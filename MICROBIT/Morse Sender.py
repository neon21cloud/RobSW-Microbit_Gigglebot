from microbit import *
import radio


def main():

    display.show(Image.TRIANGLE)
    radio.on()

    while True:
        radio.config(power=7, group=10)
        if button_a.was_pressed():
            radio.send('dot')

        if button_b.was_pressed():
            radio.send('dash')


if __name__ == "__main__":
    main()