#Programa que hace que el GiggleBot avance por una línea con curvas.

from microbit import *
import gigglebot

def main():

    gigglebot.set_speed(50, 50)
    gigglebot.init()
    THRESHOLD = 275

    finish = False
    while not finish:

        values = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)

        #Si los valores del sensor de linea son menores que el limite, la superficie es oscura y puedo avanzar.
        #Esto lo indican los LEDS encendiendose de verde.

        if (values[0] and values[1]) < THRESHOLD:

            gigglebot.drive(gigglebot.FORWARD, 100)
            gigglebot.set_smile(0, 255, 0)

            #Lógica de los giros:

            # Giros a la izquierda
            if values[0] > THRESHOLD:
                gigglebot.turn(gigglebot.LEFT, 100)
                gigglebot.drive(gigglebot.FORWARD, 100)

            # Giros a la derecha
            if values[1] > THRESHOLD:
                gigglebot.turn(gigglebot.RIGHT, 100)
                gigglebot.drive(gigglebot.FORWARD, 100)

        #Si los valores del sensor de linea son mayores que el limite, la superficie es clara y retrocedo.
        #Esto lo indican los LEDS encendiendose de rojo.
        else:
            gigglebot.drive(gigglebot.BACKWARD, 100)
            gigglebot.set_smile(255, 0, 0)

            #Lógica de los giros marcha atrás:

            if (values[1] < THRESHOLD) and (values[0] > THRESHOLD):
                gigglebot.turn(gigglebot.LEFT, 150)

            if (values[1] > THRESHOLD) and (values[0] < THRESHOLD):
                gigglebot.turn(gigglebot.RIGHT, 150)

        # Puedes terminar el programa pulsando A o B.
        if button_a.was_pressed() or button_b.was_pressed():
            finish = True

if __name__ == "__main__":
    main()