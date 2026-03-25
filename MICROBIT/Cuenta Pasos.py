from microbit import *

def main():

    steps = 0
    APAGA = False

    while not APAGA:

        if accelerometer.get_y() > 1500:
            steps = steps + 1
            display.show(str(steps))

        if button_a.is_pressed():
            steps=0

        if button_b.is_pressed():
            display.clear()
            APAGA=True

if __name__ == "__main__":
    main()