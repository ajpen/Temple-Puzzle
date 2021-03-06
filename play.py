import sys
import time
import signal
import RPi.GPIO as GPIO


from ledcontrol import LEDoff, LEDon
from puzzles import Puzzles
from SequentialReader import SequentialReader
Reader = SequentialReader()

LEFT_LED = 13
RIGHT_LED = 16
CORRECT_LED = 33
WRONG_LED = 31


def reset_LEDs():
    LEDoff(LEFT_LED)
    LEDoff(RIGHT_LED)
    LEDoff(CORRECT_LED)
    LEDoff(WRONG_LED)


def safe_exit(*args, **kwargs):
    reset_LEDs()
    GPIO.cleanup()

signal.signal(signal.SIGINT, safe_exit)

def read_left():
    while True:
        first = Reader.ReadCE0()
        time.sleep(2)
        if Reader.ReadCE0() == first:
            LEDon(LEFT_LED)
            return first


def read_right():
    while True:
        first = Reader.ReadCE1()
        time.sleep(2)
        if Reader.ReadCE1() == first:
            LEDon(RIGHT_LED)
            return first


if __name__=="__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: play.py [GameNumber]")

    game_id = int(sys.argv[1]) - 1
    game = Puzzles[game_id]

    left_input = None
    right_input = None
    lives = 3

    while lives > 0:
        left_input = read_left()
        right_input = read_right()

        if left_input == game[0] and right_input == game[1]:
            LEDon(CORRECT_LED)
            time.sleep(10)
            safe_exit()
            sys.exit(0)

        else:
            lives = lives - 1
            LEDon(WRONG_LED)
            time.sleep(5)
            reset_LEDs()
