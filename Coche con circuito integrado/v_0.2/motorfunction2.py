# importamos las librerias
import RPi.GPIO as GPIO
import time 
import os
import PantallaControl as control

# configuramos a modo de pin
GPIO.setmode (GPIO.BOARD)

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

# definimos los pines de salida en este caso
GPIO.setup(AdelanteM1 ,GPIO.OUT) #motor IZQ delante
GPIO.setup(AtrasM1,GPIO.OUT) #motor IZQ atras
GPIO.setup(AdelanteM2, GPIO.OUT) #motor DER delante
GPIO.setup(AtrasM2, GPIO.OUT) #motor DER atras

M1_vel(control.joystick.x,control.joystick.x)
M2_vel(control.joystick.x,control.joystick.x)


def M1_vel (joyX_M1,joyY_M1): # motor "derecha"
	xx

def M2_vel (joyX_M2,joyY_M2): #motor "izquierda"
	yy













