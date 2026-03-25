from gigglebot import *
from utime import ticks_us, sleep_us
import ustruct
import radio

# stop the robot if it's already moving
stop()
# enable radio
radio.on()


while True:

    try:
        # read robot commands
        lmotor, rmotor = ustruct.unpack('bb', radio.receive_bytes())

        # and actuate the motors should there be any received commands
        set_speed(lmotor, rmotor)
        drive()
    except TypeError:
        pass