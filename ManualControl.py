import time as time
import ClassMOTOR

x=1
y=2
z=3

m1=ClassMOTOR.Motor2(x, y, z)
m2=ClassMOTOR.Motor2(6,5,22)
m3=ClassMOTOR.Motor2(16,12,25)
m4=ClassMOTOR.Motor2(x, y, z)
m5=ClassMOTOR.Motor2(26,19,13)
m6=ClassMOTOR.Motor2(24,23,18)

def init():
    m1.moveCCW(90)
    time.sleep(0.08)
    m2.moveCW(90)
    time.sleep(0.08)
    m3.moveCW(90)
    time.sleep(0.08)
    m5.moveCW(90)
    time.sleep(0.08)
    m6.moveCW(90)

def position1():
    m2.moveCW(90)
    time.sleep(0.08)
    m3.moveCW(90)
    time.sleep(0.08)
    m5.moveCW(120)
    time.sleep(0.08)
    m6.moveCW(90)
    flag1 = 1


def position1R():
    m2.moveCCW(90)
    time.sleep(0.08)
    m3.moveCCW(90)
    time.sleep(0.08)
    m5.moveCCW(120)
    time.sleep(0.08)
    m6.moveCCW(90)
    flag1 = 0


def position2():
    m1.moveCW(180)
    time.sleep(0.08)
    m2.moveCW(90)
    time.sleep(0.08)
    m3.moveCW(90)
    time.sleep(0.08)
    m5.moveCW(120)
    time.sleep(0.08)
    m6.moveCW(90)
    flag2 = 1


def position2R():
    m1.moveCCW(180)
    time.sleep(0.08)
    m2.moveCCW(90)
    time.sleep(0.08)
    m3.moveCCW(90)
    time.sleep(0.08)
    m5.moveCCW(120)
    time.sleep(0.08)
    m6.moveCCW(90)
    flag2 = 0


def position3():
    m1.moveCCW(180)
    time.sleep(0.08)
    m2.moveCW(90)
    time.sleep(0.08)
    m3.moveCW(90)
    time.sleep(0.08)
    m5.moveCW(120)
    time.sleep(0.08)
    m6.moveCW(90)
    flag3 = 1


def position3R():
    m1.moveCW(180)
    time.sleep(0.08)
    m2.moveCCW(90)
    time.sleep(0.08)
    m3.moveCCW(90)
    time.sleep(0.08)
    m5.moveCCW(120)
    time.sleep(0.08)
    m6.moveCCW(90)
    flag3 = 0

    
def initState():
    if flag1 == 0 and flag2 ==0 and flag3==0:
        init()
    elif flag1 == 1:
        position1R()
    elif flag2 == 1:
        position2R()
    elif flag3 == 1:
        position3R()
    
    
    
def scenario1():
    position1()
    initState()

def scenario2():
    position2()
    initState()

def scenario3():
    position3()
    initState()

