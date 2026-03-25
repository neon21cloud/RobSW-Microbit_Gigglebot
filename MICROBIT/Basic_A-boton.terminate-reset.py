from microbit import *

def main():
    while not button_a.is_pressed():
        display.show(Image.HAPPY)
        if accelerometer.was_gesture("shake"):
            display.show(Image.SAD)
            sleep(2000)

    display.clear()
    sleep(1000)
    display.show("FIN. Pulsa reset para reiniciar")

if __name__ == "__main__":
    main()