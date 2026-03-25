#Programa que hace que el robot dibuje en el suelo un círculo de unos 40 cm de radio.

from microbit import *
import gigglebot

def main():
    while True:

        RADIO = 40
        PERIM = 6.18*RADIO          # A partir del radio calculo en perimetro de la cicunferencia
        LADOS_DEL_POLIGONO = 20     # Elijo aproximar el circulo a un poligono de 20 lados
        LONG_DEL_LADO = PERIM/LADOS_DEL_POLIGONO
        GIRO = 360/LADOS_DEL_POLIGONO # Para calcular los grados de giro, divido 360º entre los lados del poligono
        AVANZO = LONG_DEL_LADO*8

        gigglebot.turn(gigglebot.RIGHT, GIRO)
        gigglebot.set_speed(50, 50)
        gigglebot.drive(gigglebot.FORWARD, AVANZO)

if __name__ == "__main__":
    main()