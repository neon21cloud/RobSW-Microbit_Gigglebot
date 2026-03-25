#Programa que te permite guiar el GiggleBot con una mano por delante de él, de forma que se acercan a la mano
#según la vas alejando, pero se para si está a menos de 10cm de tu mano.

from microbit import *
import gigglebot
import distance_sensor

def main():

    ds = distance_sensor.DistanceSensor()
    LIMIT = 150 #Unos 10 cm de distancia
    SEPARACION_MAX = 400 #Maximo de distancia al que puedes poner la mano para que el gigglebot te haga caso

    while True:

        distance = ds.read_range_single()

        #Si detecta la mano a menos de 10cm o si la detecta a mas de 40cm, el coche se para.
        if distance < LIMIT or distance > SEPARACION_MAX:
            gigglebot.stop()

        else:
            gigglebot.drive(gigglebot.FORWARD)


if __name__ == "__main__":
    main()