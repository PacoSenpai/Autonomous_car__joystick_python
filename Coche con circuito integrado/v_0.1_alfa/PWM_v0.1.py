# importamos las librerias
import RPi.GPIO as pin
import time 
import os

pin.setmode (GPIO.BOARD)
RM_A = 7
RM_B = 11
LM_A = 13
LM_B = 15

GPIO.setup(RM_A ,GPIO.OUT)
GPIO.setup(RM_B,GPIO.OUT) 
GPIO.setup(LM_A, GPIO.OUT) 
GPIO.setup(LM_B, GPIO.OUT)

pwm_L = pin.PWM(12,100)
pwm_R = pin.PWM(12,100)
#funciones de los motores

