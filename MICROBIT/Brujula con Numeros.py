from microbit import *

#compass.calibrate()

while True:
    #needle = ((15 - compass.heading()) // 30) % 12
    #display.show(Image.ALL_CLOCKS[needle])


    grado = compass.heading()
    display.scroll(str(grado))
