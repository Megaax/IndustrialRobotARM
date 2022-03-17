import math
import RPi.GPIO as GPIO
import time

# ground enable pin
# set direction of motor
# determine the angle of rotation (200 steps for a 360deg)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor2:

  def __init__(self, direction, cw, en):
    self.direction = direction
    self.cw = cw
    self.en = en
    GPIO.setup(self.cw, GPIO.OUT)
    GPIO.setup(self.direction, GPIO.OUT)
    GPIO.setup(self.en, GPIO.OUT)


  def moveCW(self, angel, delay):
      #GPIO.output(self.en, GPIO.LOW)    #ENABLE PIN IS ACTIVE LOW
      GPIO.output(self.cw, GPIO.LOW)
      steps = math.floor((angel * 200) / 360)
      steps*=20

      for i in range(steps):
        GPIO.output(self.direction, GPIO.LOW)
        #@time.sleep(delay)
        GPIO.output(self.direction, GPIO.HIGH)
        time.sleep(delay)



        
  def moveCCW(self, angel, delay):
      GPIO.output(self.cw, GPIO.HIGH)
      GPIO.output(self.en, GPIO.LOW)
      steps = math.floor((angel * 200) / 360)
      steps*=20
      for i in range(steps):
        GPIO.output(self.direction, GPIO.LOW)
        #time.sleep(delay)
        GPIO.output(self.direction, GPIO.HIGH)
        time.sleep(delay)

      #GPIO.output(self.en, GPIO.LOW)




    
