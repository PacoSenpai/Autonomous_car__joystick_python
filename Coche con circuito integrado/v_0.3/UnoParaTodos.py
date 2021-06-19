from tkinter import *
#import RPi.GPIO as pin
import time 
import os

# variables globales

mouse_inscreen = 10
joyX = 0
joyY = 0

############################ FUNCIONES VARIAS ###################################################################

def joystick (vector): # joystick
	
	joyX = int(vector.x*(2/3)-100)
	joyY = int(vector.y*(-2/3)+100)
	mouse_inscreen = 1
	if joyX > 100 or joyX < -100 :
		joyX = 0
		joyY = 0
		mouse_inscreen = 0
		
	if joyY > 100 or joyY < -100 :
		joyX = 0
		joyY = 0
		mouse_inscreen = 0

	print ("click en:",joyX,joyY)
	print (mouse_inscreen)

############################### MOTORES ##################################################################





############################## PANTALLA ###################################################################

root = Tk()
root.title("DeltaDynamics'robot")
root.geometry("600x600")
root.config(bg="#3DC3D8")
root.config(bd=10)
root.config(relief="groove")

os.system ("cls") 

frame = Frame(root, width = 300, height =300)
frame.bind("<B1-Motion>", joystick)
frame.config(relief="groove")
frame.config(bd=10)
frame.pack()

#Label(root, text=("x = ",joyX).pack()
#Label(root, text="¡Hola Mundo!").pack() 

#botones
'''button_Right = Button(right_box, padx=25, pady=15, text="--------->>", comand = motor.rigth)
button_Right.pack(padx=0, pady=0)'''



root.mainloop()




