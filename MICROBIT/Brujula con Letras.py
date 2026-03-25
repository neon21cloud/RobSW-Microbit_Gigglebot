from microbit import *

#compass.calibrate()

while True:

    grado = compass.heading()

    if grado >= 350 or grado <= 10:

        display.show("N", delay=1000, clear=True)

    elif grado >= 80 and grado <= 110:

        display.show("E", delay=1000, clear=True)

    elif grado >= 170 and grado <= 190:

        display.show("S", delay=1000, clear=True)

    elif grado >= 260 and grado <= 280:

        display.show("W", delay=1000, clear=True)