import sys
import time
import signal

from ledcontrol import LEDoff, LEDon
from puzzles import Puzzles
from SequentialReader import SequentialReader
Reader = SequentialReader()

LEFT_LED = 13
RIGHT_LED = 15
CORRECT_LED = 31
WRONG_LED = 33


def reset_LEDs():
    LEDoff(LEFT_LED)
    LEDoff(RIGHT_LED)
    LEDoff(CORRECT_LED)
    LEDoff(WRONG_LED)


def safe_exit():
    reset_LEDs()

signal.signal(signal.SIGINT, safe_exit())

def read_left():
    while True:
        first = Reader.ReadCE0()
        time.sleep(5)
        if Reader.ReadCE0() == first:
            LEDon(LEFT_LED)
            return first


def read_right():
    while True:
        first = Reader.ReadCE1()
        time.sleep(5)
        if Reader.ReadCE1() == first:
            LEDon(RIGHT_LED)
            return first


if __name__=="__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: play.py [GameNumber]")

    game_id = int(sys.argv[1])
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
            reset_LEDs()
            sys.exit(0)

        else:
            lives = lives - 1
            LEDon(WRONG_LED)
            time.sleep(2)
            reset_LEDs()
