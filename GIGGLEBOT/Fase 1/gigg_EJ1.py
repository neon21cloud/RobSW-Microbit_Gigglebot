#Programa que muestra en la sonrisa del gigglebot los colores rotando entre todas las posiciones.

from microbit import *
import gigglebot

def main():

    #Inicializo los colores
    strip = gigglebot.init()
    strip[2] = (255, 0, 0)
    strip[3] = (0, 0, 255)
    strip[4] = (0, 255, 0)
    strip[5] = (255, 255, 0)
    strip[6] = (0, 255, 255)
    strip[7] = (255, 0, 255)
    strip[8] = (20, 20, 20)

    #Bucle de rotación
    while True:

        i = strip[8]
        strip[8]=strip[2]
        strip[2]=strip[3]
        strip[3]=strip[4]
        strip[4]=strip[5]
        strip[5]=strip[6]
        strip[6]=strip[7]
        strip[7]=i

        sleep(200)
        strip.show()

if __name__ == "__main__":
    main()