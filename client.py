# Imports go at the top
from microbit import *

def setup():
    uart.init(115200)


def main():
    # Code in a 'while True:' loop repeats forever
    while True:
        if button_a.was_pressed():
            if temperature() < 10:
                uart.write('0' + str(temperature()))
            else:
                uart.write(str(temperature()))

setup()
main()
