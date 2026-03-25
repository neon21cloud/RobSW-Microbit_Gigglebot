#Programa que puede funcionar como GiggleBot Maestro o como Seguidor. El GiggleBot en modo Maestro envía
#por radio instrucciones de movimiento que siguen los robots que estén en modo Seguidor.

from microbit import *
import gigglebot
import radio

def Avanzo():
    gigglebot.drive(gigglebot.FORWARD, 1000)

def Izquierda():
    gigglebot.turn(gigglebot.LEFT, 500)

def Derecha():
    gigglebot.turn(gigglebot.RIGHT, 500)

def Stop():
    gigglebot.stop()


def main():

    POTENCIA = 7
    GRUPO = 42
    Orden = 0
    radio.on()
    radio.config(power=POTENCIA, group=GRUPO)
    gigglebot.set_speed(50, 50)

    while True:

        #Modo MAESTRO
        if button_a.is_pressed():

            strip = gigglebot.init()
            display.show("M")
            strip[0] = (255, 0, 0)
            strip[1] = (255, 0, 0)
            strip.show()
            gigglebot.set_smile(255, 0, 0)

            Pressed = True
            while Pressed:

                Orden = 'Lucas-1'
                radio.send(Orden)
                Avanzo()

                Orden = 'Lucas-2'
                radio.send(Orden)
                Izquierda()

                Orden = 'Lucas-3'
                radio.send(Orden)
                Derecha()

                Orden = 'Lucas-1'
                radio.send(Orden)
                Avanzo()

                Orden = 'Lucas-2'
                radio.send(Orden)
                Izquierda()

                Orden = 'Lucas-4'
                radio.send(Orden)
                Stop()

                Pressed = False


        #Modo SEGUIDOR
        if button_b.is_pressed():

            strip = gigglebot.init()
            display.show("S")
            strip[0] = (0, 255, 0)
            strip[1] = (0, 255, 0)
            strip.show()
            gigglebot.set_smile(0, 255, 0)

            while True:

                received = radio.receive_full()
                if received != None:
                    msg, dBm, _ = received
                    Identificador = str(msg[3:8], 'utf8')

                    if Identificador == 'Lucas':

                        Instruccion = str(msg[9:], 'utf8')

                        if Instruccion == '1':
                            Avanzo()

                        if Instruccion == '2':
                            Izquierda()

                        if Instruccion == '3':
                            Derecha()

                        if Instruccion == '4':
                            Stop()


if __name__ == "__main__":
    main()



