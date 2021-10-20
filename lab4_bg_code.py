import RPi.GPIO as GPIO
import json
import time

ledPins = [17, 27, 22]
pwm = []

GPIO.setmode(GPIO.BCM)
for i in range(len(ledPins)):
  GPIO.set(ledPins[i], GPIO.OUT)
  pwm.append(GPIO.PWM(ledPins[i],100))
  pwm[i].start(0)

while True:
  with open("lab4.text",'r') as f:
    data = json.load(f)
  pwm[data["led"]-1].ChangeDutyCycle(data["slider"])
  time.sleep(0.1)
    
    