from microbit import*


def get_xy(): #Posicion de x e y en todo momento

    yaccel = accelerometer.get_y() * accelerometer_sensitivity
    xaccel = accelerometer.get_x() * accelerometer_sensitivity
    return yaccel, xaccel


def count_lit_pixels(): #Contador de pixeles encendidos
    pixel_count = 0
    for xx in range (5):
        for yy in range (5):
            if display.get_pixel(xx, yy) != 0:
                pixel_count = pixel_count + 1
    return pixel_count



def main():

    FIN = 50
    nivel = 1
    global accelerometer_sensitivity
    accelerometer_sensitivity = 1/250
    j = 3

    #Posicion inicial
    x, y = 2, 2

    yaccel, xaccel = get_xy()
    y = max(0, min(4, int(y + yaccel)))
    x = max(0, min(4, int(x + xaccel)))
    #----------------------------------

    display.scroll("LLENA LA PANTALLA")
    for i in range (3):
        display.show(j, delay=500, clear=True)
        j = j - 1


    while FIN > 0:

        # Nueva posicion
        yaccel, xaccel = get_xy()
        newy = max(0, min(4, int(y + yaccel)))
        newx = max(0, min(4, int(x + xaccel)))


        #Si la nueva posicion es distinta a la anterior, iluminar pixel suave
        #Tu posicion se indica con un pixel mas iluminado
        if newy != y or newx != x:
            display.set_pixel(x, y, 7)
            x, y = newx, newy
            display.set_pixel(x, y, 9)
        else:
            display.set_pixel(newx, newy, 9)
        #-------------------------------------


        #Si el numero de pixeles iluminados es 25 (todos), te lo has pasado
        pixels = count_lit_pixels()
        if pixels == 25:

            nivel = nivel + 1                  #Subes de nivel
            FIN = FIN - 5
            accelerometer_sensitivity = accelerometer_sensitivity * 0.90
            sleep(200)
            display.show(str(nivel))
            sleep(1000)
            display.clear()

        sleep(FIN)

    display.scroll('VICTORIA') #Cuando FIN llegue a 0, es decir, tras 10 rondas, ganas
    display.show(Image.HAPPY)

if __name__ == "__main__":
    main()



