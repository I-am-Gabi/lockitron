import RPi.GPIO as GPIO
import time

def buttonPressed(a):
    print(a)
    print('button pressed')

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.cleanup()

    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(40, GPIO.FALLING, bouncetime=1000, callback=buttonPressed)

if __name__ == '__main__':
    main()
