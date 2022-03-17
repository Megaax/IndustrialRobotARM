import RPi.GPIO as GPIO
import time


PWMpin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMpin, GPIO.OUT)
#sets servo to pwm to 50hz pulse

servo = GPIO.PWM(PWMpin, 50)
servo.start(0)


def move(angle):
    duty = 2
    steps = 2+(angle/18)
    while duty <= steps:
        servo.ChangeDutyCycle(steps)
        # time to make servo turns
        time.sleep(0.3)
        print("a7a")
        # hold servo at current position
        #servo.ChangeDutyCycle(0)
        duty = duty + 1

def hold():
    move(0)
    time.sleep(0.5)
    move(45)
    
def let():
    move(0)
    time.sleep(0.5)
    move(180)
'''
def pick(): 
    init_data = detect_init()
    #when camera sends the grid and the state move scenarios 
    while True:
        data = detect(init_data)
        if data[0]:
            detect_end(init_data[0])
            break
    print(data[1])
    if data[1] == 1:
        hold()
 '''       
def place():
    let()

def pickplace():
    pick()
    time.sleep(1)
    let()


class ServoClass:

    def __init__(self, pin):
        self.pin = pin
        serv = GPIO.PWM(PWMpin, 50)
        serv.start(0)


    def move(angle):
        duty = 2
        steps = 2+(angle/18)
        while duty <= steps:
            serv.ChangeDutyCycle(steps)
            # time to make servo turns
            time.sleep(0.3)
            print("IN MOVE ")
            # hold servo at current position
            #servo.ChangeDutyCycle(0)
            duty = duty + 1


