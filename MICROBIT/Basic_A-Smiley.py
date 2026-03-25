from microbit import *
def main():
    number_sad = 0
    while True:
            display.show(Image.HAPPY)

            if accelerometer.was_gesture("shake"):
                display.show(Image.SAD)
                number_sad = number_sad + 1
                sleep(2000)

            if button_b.is_pressed():
                print("number_sad: " + str(number_sad))


if __name__ == "__main__":
    main()