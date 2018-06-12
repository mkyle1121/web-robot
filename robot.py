#!/usr/bin/env python

import easygopigo3
import time

gpg = easygopigo3.EasyGoPiGo3()
servo = gpg.init_servo(port="SERVO1")
servo2 = gpg.init_servo(port='SERVO2')

def forward():
	gpg.forward()
	time.sleep(1)
	gpg.stop()	

def backward():
	gpg.backward()
	time.sleep(1)
	gpg.stop()

def stop():
	gpg.stop()

def left():
	gpg.left()
	time.sleep(1)
	gpg.stop()

def right():
	gpg.right()
	time.sleep(1)
	gpg.stop()

def servo_left():
	servo.rotate_servo(140)
	time.sleep(.1)
	servo2.rotate_servo(140)

def servo_center():
	servo.rotate_servo(96)
	time.sleep(.1)
	servo2.rotate_servo(96)

def servo_right():
	servo.rotate_servo(60)
	time.sleep(.1)
	servo2.rotate_servo(60)

def blinkers():
	for i in range (30):
		gpg.blinker_on(0)
		time.sleep(.1)
		gpg.blinker_off(0)
		gpg.blinker_on(1)
		time.sleep(.1)
		gpg.blinker_off(1)

def lights():
	for i in range(10):
		gpg.set_eye_color((255,0,0))
		gpg.open_eyes()
		time.sleep(.1)
		gpg.set_eye_color((0,255,0))
		gpg.open_eyes()
		time.sleep(.1)
		gpg.set_eye_color((0,0,255))
		gpg.open_eyes()
		time.sleep(.1)
		gpg.close_eyes()

