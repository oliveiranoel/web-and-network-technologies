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

        if button_b.was_pressed():
            room_number += 1
            uart.write('nr')

        if button_a.is_pressed() and button_b.is_pressed():
            uart.write('rr')


setup()
main()
