from microbit import*


def get_xy(): #Posicion de x e y en todo momento

    yaccel = accelerometer.get_y() * accelerometer_sensitivity
    xaccel = accelerometer.get_x() * accelerometer_sensitivity
    return yaccel, xaccel


def count_lit_pixels(): #Contador de pixeles encendidos

    global xx
    global yy

    pixel_count = 0
    for xx in range (5):
        for yy in range (5):
            if FIN > 25:
                if display.get_pixel(xx, yy) != 0:
                    pixel_count = pixel_count + 1
            if FIN <= 25:
                if display.get_pixel(xx, yy) == 7:
                    pixel_count = pixel_count + 1

    return pixel_count


def main():

    global FIN
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
        #El pixel que marca tu posicion se ilumina mas fuerte

        if FIN > 25:
            if newy != y or newx != x:
                display.set_pixel(x, y, 7)
                x, y = newx, newy
                display.set_pixel(x, y, 9)

        if FIN <= 25:
            if newy != y or newx != x:
                display.set_pixel(x, y, 2)
                if display.get_pixel(newx, newy) == 2:
                    display.set_pixel(x, y, 7)
                if display.get_pixel(newx, newy) == 7:
                    display.set_pixel(x, y, 7)
                x, y = newx, newy
                display.set_pixel(x, y, 9)


        else:
            display.set_pixel(newx, newy, 9)
        #-------------------------------------


        #Si el numero de pixeles iluminados es 25 (todos), te lo has pasado
        pixels = count_lit_pixels()

        if FIN > 25:
            if pixels == 25:

                FIN = FIN - 5
                nivel = nivel + 1                  #Subes de nivel
                accelerometer_sensitivity = accelerometer_sensitivity * 0.90
                sleep(200)
                display.show(Image.ALL_CLOCKS, delay = 350, clear=True)
                display.show(str(nivel))
                sleep(1000)
                display.clear()

        if FIN <= 25:
            if pixels >= 24:

                FIN = FIN - 5
                nivel = nivel + 1                  #Subes de nivel
                accelerometer_sensitivity = accelerometer_sensitivity * 0.90
                sleep(200)
                display.show(Image.ALL_CLOCKS, delay = 350, clear=True)
                display.show(str(nivel))
                sleep(1000)
                display.clear()

        #sleep(FIN)


    display.scroll('VICTORIA') #Cuando FIN llegue a 0, es decir, tras 10 rondas, ganas
    display.show(Image.HAPPY)


    # BUG REPORT:
    # -- Salta del nivel 6 al 7 sin jugar aunque muestra el reloj de carga
    # -- Reloj de carga antes del mensaje de Victoria
    # -- Aparece un 1 antes del mensaje de Victoria
    # -- Meter un mensaje para un nivel lo deja en loop y no puedes seguir


if __name__ == "__main__":
    main()