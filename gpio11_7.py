import time
import vidplay
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setwarnings(False)	

vidplayer = vidplay.Vidplay()


state = "Idle"
while True:
                
                
                
	if state == "Idle":
			if GPIO.input(4) == True and GPIO.input(22) == True:
				vidplayer.play(2)
				print("Active")
				state = "Active"
			
	elif state == "Active":
			if GPIO.input(4) == False and GPIO.input(22) == False:
				vidplayer.stop()
				print("Idle")
				state = "Idle"
			elif GPIO.input(4) != GPIO.input(22):
				vidplayer.pause()
				print("CoverUp")
				state = "CoverUp"
                                
	elif state == "CoverUp":
			if GPIO.input(4) == False and GPIO.input(22) == False:
				vidplayer.stop()
				print("Idle")
				state = "Idle"
			elif GPIO.input(4) == True and GPIO.input(22) == True:
				vidplayer.pause()
				print("Active")
				state = "Active"
	
	
