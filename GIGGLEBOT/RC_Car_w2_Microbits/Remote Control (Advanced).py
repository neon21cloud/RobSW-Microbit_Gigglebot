from microbit import *
import ustruct
import radio
import math


def control (motor_speed):

    radio.on()

    low = 20

    if gesture == "up": #forward

        radio.send_bytes(ustruct.pack('bb', motor_speed, motor_speed))
        display.show(Image.ARROW_N)


    elif gesture == "left":

        radio.send_bytes(ustruct.pack('bb', motor_speed, -motor_speed))
        display.show(Image.ARROW_W)


    elif gesture == "right":

        radio.send_bytes(ustruct.pack('bb', -motor_speed, motor_speed))
        display.show(Image.ARROW_E)


    elif gesture == "down": #backward

        radio.send_bytes(ustruct.pack('bb', -motor_speed, -motor_speed))
        display.show(Image.ARROW_S)


    else:
        radio.send_bytes(ustruct.pack('bb', 0, 0))
        display.show(Image.TRIANGLE)



def main():


    while True:

        global gesture
        gesture = accelerometer.current_gesture()

        stateA = button_a.is_pressed()
        stateB = button_b.is_pressed()

        if not stateA and not stateB:
            motor_speed = 50
            control(motor_speed)

        if stateA and stateB:
            motor_speed = 75
            control(motor_speed)
            display.show(Image.RABBIT)

        if stateA and not stateB:
            radio.send_bytes(ustruct.pack('bb', 50, 20))
            display.show(Image.ARROW_NW)

        if not stateA and stateB:
            radio.send_bytes(ustruct.pack('bb', 20, 50))
            display.show(Image.ARROW_NE)



if __name__ == "__main__":
    main()