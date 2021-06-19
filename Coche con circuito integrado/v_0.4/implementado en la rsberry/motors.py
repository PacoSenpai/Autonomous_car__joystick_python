#from tkinter import *
import RPi.GPIO as GPIO
import time
#import math


GPIO.setmode (GPIO.BOARD)

RM_A = 10
RM_B = 8
LM_A = 3
LM_B = 5

pin_pwm_L = 7
pin_pwm_R = 12

GPIO.setup(RM_A ,GPIO.OUT)
GPIO.setup(RM_B,GPIO.OUT) 
GPIO.setup(LM_A, GPIO.OUT) 
GPIO.setup(LM_B, GPIO.OUT)

GPIO.setup(pin_pwm_L,GPIO.OUT)
GPIO.setup(pin_pwm_R,GPIO.OUT)

pwm_L = GPIO.PWM(pin_pwm_L,100)
pwm_R = GPIO.PWM(pin_pwm_R,100)

pwm_L.start(100)
pwm_R.start(100)


def leftMotor (velL,delante1):
	pwm_L.ChangeDutyCycle(velL)
	if delante1 == 1:
		GPIO.output(LM_A,True)
		GPIO.output(LM_B,False)
		
	else:
		GPIO.output(LM_A,False)
		GPIO.output(LM_B,True)

	print(velL)
		
		
	  

def rightMotor (velR, delante2):
	pwm_R.ChangeDutyCycle(velR)
	if delante2 == 1:
		GPIO.output(RM_A,True)
		GPIO.output(RM_B,False)
	else:
		GPIO.output(RM_A,False)
		GPIO.output(RM_B,True)
	print (velR)
	

GPIO.cleanup()
