import RPi.GPIO as GPIO


def LEDon(pin):
    """from https://www.instructables.com/id/Using-a-RPi-to-Control-an-RGB-LED/"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def LEDoff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
