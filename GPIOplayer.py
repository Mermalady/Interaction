import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

if state == "Idle"
    print("Idle")
    #os.system('omxplayer -o local static.mp4 &')
    if GPIO.input(17) == True
    state = "FadeIn"
    
elif state == "FadeIn"
    print("FadeIn") 
    #os.system('omxplayer -o hdmi FadeIn.mp4 &')
    state = "Active"
    
elif state == "Active"
    print("Active")
    #os.system('omxplayer -o hdmi Page1_3.mp4 &')
    if GPIO.input(17) == False
    state = "FadeOut"

elif state == "FadeOut"
    print("FadeOut")
    #os.system('omxplayer -o hdmi FadeOut.mp4 &')
    state = "Idle"
    