#Programa que hace que el gigglebot siga la luz.

from microbit import *
import gigglebot
def main():

    OSCURIDAD = 65
    gigglebot.set_speed(50, 50)
    gigglebot.init()

    Luz = False
    while not Luz:

        #Inicializo los valores del sensor de luz.
        values = gigglebot.read_sensor(gigglebot.LIGHT_SENSOR, gigglebot.BOTH)
        val_left = values[0]
        val_right = values[1]

        #Comparo cada par de valores de los sensores de luz y muevo el coche en funcion de ello.
        for i in range(len(values)):
            i = i + 1

            if val_left < val_right:
                gigglebot.turn(gigglebot.LEFT, 200)
                gigglebot.drive(gigglebot.FORWARD, 200)
                gigglebot.set_smile(100, 0, 0)

            elif val_left > val_right:
                gigglebot.turn(gigglebot.RIGHT, 200)
                gigglebot.drive(gigglebot.FORWARD, 200)
                gigglebot.set_smile(0, 100, 0)

            #Si los valores fuesen iguales, en una zona de oscuridad retrocedo y en una de luz avanzo.
            else:
                if val_left <= OSCURIDAD:
                    gigglebot.drive(gigglebot.BACKWARD, 200)
                    gigglebot.set_smile(0, 0, 100)

                else:
                    gigglebot.drive(gigglebot.FORWARD, 200)
                    gigglebot.set_smile(0, 0, 100)


if __name__ == "__main__":
    main()