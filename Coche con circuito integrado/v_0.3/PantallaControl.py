#lo antiguo

'''from tkinter import *
#import RPi.GPIO as pin
import time 
import os

joyX = 0
joyY = 0

# da el pixel al que estas clikando
def joystick (vector):
	joyX = vector.x/3
	joyY = vector.y/3
	if joyX > 100 or joyX < 0 :
		joyX = 0
		joyY = 0
	if joyY > 100 or joyY < 0 :
		joyX = 0
		joyY = 0
	print ("click en:",joyX,joyY)

def stop (event):
        print("stop");
                

root = Tk()
root.title("DeltaDynamics'robot")
root.geometry("600x600")
root.config(bg="#FCD44E")
root.config(bd=10)
root.config(relief="groove")

frame = Frame(root, width = 300, height =300)
frame.bind("<B1-Motion>", joystick)
frame.pack()

root.bind("<Button-3>",stop)




# est es lo mismo que antes del PWM



root.mainloop()
'''


## esto es lo nuevo

from tkinter import *
#import RPi.GPIO as pin
import time 
import os

mouse_inscreen = 10
joyX = 0
joyY = 0

# da el pixel al que estas clikando

def joystick (event):
	
	joyX = event.x*(2/3)-100
	joyY = event.y*(-2/3)+100
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

root = Tk()
root.title("DeltaDynamics'robot")
root.geometry("600x600")
root.config(bg="#FCD44E")
root.config(bd=10)
root.config(relief="groove")

frame = Frame(root, width = 300, height =300)
frame.bind("<B1-Motion>", joystick)
frame.pack()

# est es lo mismo que antes del PWM


root.mainloop()





