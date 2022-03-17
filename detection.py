#!/usr/bin/python3

import cv2
import numpy as np

def detect_init():

    cap = cv2.VideoCapture(0)

    lower_blue = np.array([102,0,0])
    upper_blue = np.array([120,255,255])
    lower_green = np.array([45,0,0])
    upper_green = np.array([100,255,255])

    return(cap,lower_blue,upper_blue,lower_green,upper_green)

def trackbar ():

	def nothing(x):
		    pass

	cv2.namedWindow("track")
	cv2.createTrackbar("low_hue","track",0,255,nothing)
	cv2.createTrackbar("low_sat","track",0,255,nothing)
	cv2.createTrackbar("low_bri","track",0,255,nothing)
	cv2.createTrackbar("high_hue","track",0,255,nothing)
	cv2.createTrackbar("high_sat","track",0,255,nothing)
	cv2.createTrackbar("high_bri","track",0,255,nothing)

def detect(init_data):

    cap = init_data[0]
    lower_blue = init_data[1]
    upper_blue = init_data[2]
    lower_green = init_data[3]
    upper_green = init_data[4]

    _,img=cap.read()
	
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #lower_blue = np.array([cv2.getTrackbarPos("low_hue","track"),cv2.getTrackbarPos("low_sat","track"),cv2.getTrackbarPos("low_bri","track")])
    #upper_blue = np.array([cv2.getTrackbarPos("high_hue","track"),cv2.getTrackbarPos("high_sat","track"),cv2.getTrackbarPos("high_bri","track")])

    #lower_green = np.array([cv2.getTrackbarPos("low_hue","track"),cv2.getTrackbarPos("low_sat","track"),cv2.getTrackbarPos("low_bri","track")])
    #upper_green = np.array([cv2.getTrackbarPos("high_hue","track"),cv2.getTrackbarPos("high_sat","track"),cv2.getTrackbarPos("high_bri","track")])

    img_hsv = cv2.GaussianBlur(img_hsv,(5,5),0)

    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(img_hsv, lower_green, upper_green)

    kernel = np.ones((5,5),np.uint8)

    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    mask_blue = cv2.bitwise_not(mask_blue)
    mask_green = cv2.bitwise_not(mask_green)

    _,cnt_blue,_=cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    _,cnt_green,_=cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt_blue = sorted(cnt_blue,key=lambda x: cv2.contourArea(x)/(np.pi*(cv2.minEnclosingCircle(x)[1]**2)),reverse=True)
    cnt_green = sorted(cnt_green,key=lambda x: cv2.contourArea(x)/(np.pi*(cv2.minEnclosingCircle(x)[1]**2)),reverse=True)

    cnt_blue = [x for x in cnt_blue if cv2.contourArea(x) > 10000 and cv2.contourArea(x) < 20000]
    cnt_green = [x for x in cnt_green if cv2.contourArea(x) > 10000 and cv2.contourArea(x) < 20000]

    '''
    if cnt_blue :
        for cnt in cnt_blue :
            x,y,w,h = cv2.boundingRect(cnt)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    if cnt_green :
        for cnt in cnt_green :
            x,y,w,h = cv2.boundingRect(cnt)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",img)
    cv2.imshow("red",mask_blue)
    cv2.imshow("green",mask_green)
    '''

    data = []

    if len(cnt_blue) + len(cnt_green) == 3:
        for cnt in cnt_blue :
            data.append([0,cv2.boundingRect(cnt)[0]])
        for cnt in cnt_green :
            data.append([1,cv2.boundingRect(cnt)[0]])
        data = sorted(data,key=lambda x:x[1])
        cv2.waitKey(1)
        return ([1,data[0][0],data[1][0],data[2][0]])
    else :
        cv2.waitKey(1)
        return (0,0,0,0)
    

def detect_end(cap):
    cap.release()

    
if __name__ == '__main__' :

    init_data = detect_init()

    while True :
        try:
            data = detect(init_data)
            print(data)
        except KeyboardInterrupt :
            detect_end(init_data[0])
            break
