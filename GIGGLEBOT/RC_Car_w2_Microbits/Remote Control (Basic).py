from microbit import sleep, display, button_a, button_b
import ustruct
import radio
import math

radio.on()
motor_speed = 50
low = 20

while True:

    stateA = button_a.is_pressed()
    stateB = button_b.is_pressed()

    if stateA and stateB:
        radio.send_bytes(ustruct.pack('bb', motor_speed, motor_speed))
        print('forward')
    if stateA and not stateB:
        radio.send_bytes(ustruct.pack('bb', motor_speed, -motor_speed))
        print('left')
    if not stateA and stateB:
        radio.send_bytes(ustruct.pack('bb', -motor_speed, motor_speed))
        print('right')
    if not stateA and not stateB:
        radio.send_bytes(ustruct.pack('bb', 0, 0))
        print('stop')



