import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT)

for i in range(0, 5):
    GPIO.output(40, 1)
    print('LED on')
    time.sleep(2)
    GPIO.output(40, 0)
    print('LED off')
    time.sleep(2)

GPIO.output(40, 1)
