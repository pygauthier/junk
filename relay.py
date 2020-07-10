import RPi.GPIO as GPIO

class Relay():

    def __init__(self, **kwargs):
        self.GPIO = GPIO
        self.pins = []

        if "pins" in kwargs:
            self.pins == kwargs.get("pins")

        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.pins, GPIO.OUT)
        self.GPIO.output(self.pins, 1)

    def status(self, pin):
        if self.GPIO.input(pin) == 0:
            return True
        return False