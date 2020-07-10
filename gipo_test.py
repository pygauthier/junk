import RPi.GPIO as GPIO
from time import sleep

relay_pins = [26, 19, 13, 6]
led_pins = [21, 20, 16, 12]

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pins, GPIO.OUT)
GPIO.setup(led_pins, GPIO.OUT)
GPIO.output(relay_pins, 1)
GPIO.output(led_pins, 1)

try:
    while True:
        for pin in led_pins:
            GPIO.output(pin, 0)
            sleep(1)
            print(pin, GPIO.input(pin))
        for pin in led_pins:
            GPIO.output(pin, 1)
            sleep(1)
            print(pin, GPIO.input(pin))
except KeyboardInterrupt:
    pass
GPIO.cleanup()