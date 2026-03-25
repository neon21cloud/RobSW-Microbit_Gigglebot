#Segunda parte del programa. El gigglebot va a la meta y transfiere las balizas y secretos al arbitro.

from microbit import *
import gigglebot
import radio
import distance_sensor

def retrocede():
    gigglebot.drive(gigglebot.BACKWARD, 1250)

def gira90dd():
    gigglebot.turn(gigglebot.RIGHT, 900)

def gira90i():
    gigglebot.turn(gigglebot.LEFT, 200)

def gira90d():
    gigglebot.turn(gigglebot.RIGHT, 200)

def avanza():
    gigglebot.drive(gigglebot.FORWARD, 200)

def process(msg):
    #Rutina para asegurarnos que solo hablamos con el arbitro
    PREFIX_REPLY = "04:"

    login = False
    id_msg = msg[0:3]
    #tail = msg[3:]
    if id_msg == PREFIX_REPLY:
        login = True

    return login

def CambioFormato():
#Esta funcion se usa para cambiar a string el formato de la matriz de IDs de Balizas y sus secretos
    String = ''
    for t in range(len(Balizas)):
        if Balizas[t][0] != 0:
            String = String + "," + str(Balizas[t][0]) + ":" + str(Balizas[t][1])
    return String

def main():
    ds = distance_sensor.DistanceSensor()
    radio.on()
    global Balizas
    cuenta = 0
    GRUPO_ARB = 43
    POWER_ARB = 0
    LIMIT = 200
    SUELO_OSCURO = 100
    VAR = 1.05
    PERIOD = 1000
    LONG = 128
    NoEnviado = True
    EnMarcha = True
    StringFinal = ""
    CAB = '03:lcrespo'
    radio.config(power = POWER_ARB, group = GRUPO_ARB, length = LONG)

    # Defino aqui una variable Balizas que sirve de ejemplo de lo que el primer programa ha podido recoger.
    # Hay que metera a mano ya que el programa esta partido en dos.
    Balizas = [[107, "sec1"], [103, "sec2"], [101, "sec3"], [0, ""], [0, ""]]

    # Ahora hay que transformarla al formato que espera el arbitro---> 03:loginAlumno,idBaliza1:secreto1,idBaliza3:secreto3
    # Cambio a string el formato de la matriz de IDs de Balizas y sus secretos
    String = CambioFormato()
    StringFinal = CAB + String

    while EnMarcha:

        distance = ds.read_range_single()
        if distance < LIMIT:            #Actuar en caso de que haya un obstaculo
            retrocede()
            gira90dd()
        else:                           #Si no hay obstáculos:
            LIGHTvalues = gigglebot.read_sensor(gigglebot.LIGHT_SENSOR, gigglebot.BOTH)
            LIGHTval_left = LIGHTvalues[0]
            LIGHTval_right = LIGHTvalues[1]

            COLORvalues = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
            COLORval_left = COLORvalues[0]
            COLORval_right = COLORvalues[1]

            if COLORval_left < SUELO_OSCURO and COLORval_right < SUELO_OSCURO:  #Si el suelo es negro, paramos para hablar con el árbitro
                gigglebot.stop()
                display.show(Image.HAPPY)           #Se muestra una cara feliz cuando está en la meta

                while NoEnviado:
                    radio.send(StringFinal)

                    received = radio.receive_full()
                    if received != None:
                        msg, dBm, _ = received
                        msg = str(msg[3:], 'utf8')
                        EsArbitro = process(msg)
                        if EsArbitro == True:           #Comprueba si la conversacion es con el arbitro
                            display.scroll(msg)         #Muestra el mensaje de confirmación del árbitro
                            EnMarcha = False
                            NoEnviado = False
                    sleep(PERIOD)
            else:                                   #Si el suelo no es oscuro, dirijo el coche hacia donde la luz sea mas fuerte
                display.show("M")                   #Se muestra una M cuando está en movimiento
                gigglebot.set_speed(50, 50)

                if LIGHTval_left*VAR < LIGHTval_right:  #Con la Constante VAR, forzamos para que haya una diferencia de luz del 5% para que actúe.
                                                        #Esto lo uso porque porque incluso los cambios de luz más sutiles influyen mucho en el movimiento del coche
                    gira90i()
                    cuenta = 0

                elif LIGHTval_left > LIGHTval_right*VAR:
                    gira90d()
                    cuenta = 0

                else:
                    cuenta = cuenta + 1             #Si el coche avanza de frente tres veces seguidas, se fuerza un desvío para evitar que avance hacia la oscuridad en caso de que los sensores lean los mismos valores.
                    avanza()
                    if cuenta == 3:
                        gira90d()
                        cuenta = 0

if __name__ == "__main__":
    main()