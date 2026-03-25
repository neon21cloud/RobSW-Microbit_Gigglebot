#Primera parte del programa. El gigglebot recoge los secretos de una o verias balizas y los almacena junto con sus IDs.

from microbit import *
import radio
import gigglebot
import distance_sensor

def MidePotencia(ID):
#Esta funcion toma varias medidas de potencia de una baliza y calcula su media
#Para ello hace hasta NUMVECES lecturas (algunas se descartaran porque pueden ser de otras balizas)
#y se queda con maximo de MAX de ellas.
#Tomar todas las medidas le lleva algo de tiempo asi que mientras lo hace, muestra un pequeño diamante en el display
    POWBEACON = 7
    GRUPO = 41
    QUEUE = 1
    radio.config(power = POWBEACON, group = GRUPO, queue = QUEUE)
    MAX = 5
    NUMVECES = 15
    PERIOD = 500
    Calculado = False
    while not Calculado:
        display.show(Image.DIAMOND_SMALL)
        i = 0
        Suma_Potencias = 0
        Potencia_Media = 0
        Divisor = MAX
        Valores_Potencias = [0] * MAX
        for j in range(NUMVECES):
            received2 = radio.receive_full()
            if received2 != None:
                msg2, dBm2, _ = received2
                ID_B2 = str(msg2[6:], 'utf8')
                if ID == ID_B2 and i < MAX:
                    #display.scroll(dBm)
                    Valores_Potencias[i] = dBm2
                    i = i + 1
            sleep(PERIOD)
        for t in Valores_Potencias:
            Suma_Potencias = Suma_Potencias + t
            if t == 0:
                Divisor = Divisor-1
        if Divisor != 0:
            Potencia_Media = int(Suma_Potencias / Divisor)
            return Potencia_Media
            Calculado = True

#Lógica de movimientos del coche
def avanza():
    gigglebot.set_speed(50, 50)
    gigglebot.drive(gigglebot.FORWARD, 3500)

def gira180():
    gigglebot.set_speed(0, 50)
    gigglebot.drive(gigglebot.FORWARD, 1950)

def retrocede():
    gigglebot.set_speed(50, 50)
    gigglebot.drive(gigglebot.BACKWARD, 1250)

def gira90d():
    gigglebot.set_speed(0, 50)
    gigglebot.turn(gigglebot.RIGHT, 900)

def muevo_coche(PotNueva, PotAnter):
# Comparo la potencia nueva con la potencia anterior y actúo en consecuencia,
# esquivando obstáculos en caso de que hubiese alguno. Los valores de potencia los envía main con los datos obtenidos de la
# función anterior MidoPotencia()

    LIMIT = 450   # Distancia de choque
    display.scroll(PotNueva, delay=100)  #Muestra la Potencia Nueva en el microbit para entender por qué el coche hace cada movimiento.
                                        #Si no se entretiene mostrandola en el display, el coche se mueve mas rápido y fluido
    if PotNueva > PotAnter:
        distance = ds.read_range_single()
        if distance < LIMIT:
            retrocede()
            gira90d()
        avanza()
    if PotNueva < PotAnter:
        gira180()
        distance = ds.read_range_single()
        if distance < LIMIT:
            retrocede()
            gira90d()
        avanza()
    if PotNueva == PotAnter:
        gira90d()
        distance = ds.read_range_single()
        if distance < LIMIT:
            retrocede()
            gira90d()
        avanza()

def intercambio_secreto(ID):
#Intercambio de secreto con una baliza. Funciona una vez que estoy lo suficientemente cerca de la baliza y por tanto, se comunica por el grupo ID de la baliza.
#A pesar de definir una QUEUE=1 en la radio, a veces quedan otros mensajes guardados que afectan al programa. Por eso apago y enciendo la radio cada vez.
    radio.off()
    radio.on()
    Lotengo = False
    POW_QUEUE = 1
    SECRET_REQUEST = "01:dameSecreto"
    PERIOD = 1000
    while not Lotengo:  #Mientras no tenga el secreto, escucho lo que envia la baliza y le envío el SECRET_REQUEST en el grupo ID correspondiente
        radio.config(power = POW_QUEUE, group = ID, queue = POW_QUEUE)
        radio.send(SECRET_REQUEST)
        for i in range(5):
            received1 = radio.receive_full()
            if received1 != None:
                msgScr1, dBmScr1, _ = received1
                SECRET_MSG = str(msgScr1[6:], 'utf8')
                if SECRET_MSG != SECRET_REQUEST:    #Es otro control para evitar ruido de la cola. No debería hacer falta pero en algunas pruebas
                    display.scroll(SECRET_MSG)
                    return SECRET_MSG
                    Lotengo = True
            sleep(PERIOD)

def main():
#ESTRATEGIA GENERAL: Elegir una de las balizas localizada y no pasar a la siguiente hasta acercarse a ella y recoger su secreto

    radio.on()
    POWBEACON = 7
    GRUPO = 41
    COLA = 1
    global ds
    global distance
    ds = distance_sensor.DistanceSensor()
    MAX = 5                         #máximo numero de balizas almacenables (porque la memoria no dá para más)
    Balizas = [[0, 0]] * MAX        #Aqui almzacenaremos los IDs de balizas y sus secretos
    # Balizas = [[106, "secreto1"], [206, "secreto2"], [101, "secreto3"], [90, "secreto4"], [0, ""]]
    codigo = "a"
    Intentosdelectura = 0           #Numero de intentos de leer balizas. La rutina hará hasta 2*MAX.
    Estantodas = False              # Variable de control para saber si ya tenemos todas las balizas
    POTMINHABLARBALIZA = -55        # Potencia minima de señal recibida a partir de la cual hablaremos con las balizas
    PERIOD = 1000

    #Mientras no tenga todas las balizas completas con IDs y secretos:
    while not Estantodas:
        radio.config(power = POWBEACON, group = GRUPO, queue = COLA)
        received = radio.receive_full()     # Me pongo a recibir señales por la radio
        metido = 0
        yaesta = 0
        Media_Anterior = 0
        if received != None:
            msg, dBm, _ = received
            ID_B = str(msg[6:], 'utf8')     #saco el ID de la baliza y lo muestro en el display
            if ID_B.isdigit() == True:      #solo acepto el ID si es un numero entero. Evito asi leer mensajes viejos de la cola de la radio
                Intentosdelectura = Intentosdelectura + 1
                display.scroll('ID:')
                display.scroll(ID_B)
                for i in range(MAX):
                    if ID_B == Balizas[i][0]:
                        yaesta = 1              #Si el ID de la baliza ya está en la matriz, pongo la variable a 1
            else:
                yaesta = 1       #si el ID leido no es un ID de baliza, le digo a la funcion que ya esta metido y que lo ignore
            #Cuando leo un ID de baliza, miro toda la lista de IDs que tengo y la añado en función de si el ID es nuevo (yaesta = 0),
            #si hay hueco en la matriz (valores de ID=0) y si no la he metido aun (metido=0) al principio del barrido de la lista.
            #Si cumple todo, lo meto en la variable Balizas
            for i in range(MAX):
                if Balizas[i][0] == 0 and metido == 0 and yaesta == 0:
                    Balizas[i] = [ID_B, 0]
                    metido = 1          #Si cumple las condiciones, meto el ID con el secreto = 0 (de momento) y le indico que ya está metido

            #Ahora ya tengo la lista de balizas (IDs). Ahora me fijo en los secretos.
            for i in range(MAX):
                if Balizas[i][0] == ID_B:       # Si el ID de baliza de la que recibo señal lo tengo registrado pero no tengo secreto...
                    while Balizas[i][1] == 0:   #Mientras no sepa su secreto:
                        #Mido su potencia media
                        PotMed = MidePotencia(ID_B)
                        #Si la potencia media esta lo suficientemente cerca de la baliza, intercambio el secreto
                        if PotMed >= POTMINHABLARBALIZA:
                            codigo = intercambio_secreto(int(ID_B)) # Envio a la funcion el ID para asegurar que la conversación es solo con la baliza que queremos
                            Balizas[i][1] = codigo
                        else:
                            #Si no estoy suficientemente cerca, muevo el coche pasandole a la funcion la potencia media nueva y la anterior
                            muevo_coche(PotMed, Media_Anterior)
                            Media_Anterior = PotMed
        sleep(PERIOD)
        if Intentosdelectura > 2*MAX:
            Estantodas = True

#El resultado final se almacena en la variable Balizas
#Balizas = [[106, "secreto1"], [206, "secreto2"], [101, "secreto3"], [90, "secreto4"], [0, ""]]
    display.scroll('Fin:')
    for i in range(MAX):
        display.scroll(Balizas[i][0])
        display.scroll(Balizas[i][1])

#AQUI CONTINUARIAMOS CON LA SEGUNDA PARTE DEL PROGRAMA, QUE ES LA QUE MUEVE LOS COCHES HASTA EL ARBITRO Y LE ENTREGA TODOS LOS IDS Y SUS SECRETOS
if __name__ == "__main__":
    main()