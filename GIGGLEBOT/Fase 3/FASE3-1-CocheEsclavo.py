#Primera parte de la fase tres. Se trata de un esfuerzo de busqueda en equipo para DOS COCHES. Se asignan dos roles: Jefe y Esclavo.
#El Jefe es el único que busca nuevas balizas y se las reparte entre los dos para buscar secretos.

#Este es el programa del del Coche-Esclavo.
#Dada la limitación de memoria, el programa solo contempla la comunicación que tiene lugar entre los dos gigglebots y omite las partes de movimiento.
#aunque esta estructurado de tal manera que de haber más memoria pudiese implementarse el movimiento sin otras modificaciones.
#Asume que puede hablar con las balizas desde cualquier punto de la habitación.

from microbit import *
import radio

def intercambio_secreto(ID):
#Rutina ya usada en otras fases para hablar con las balizas
    radio.off()
    radio.on()
    Lotengo = False
    POWBEACONSEC = 1
    SECRET_REQUEST = "01:dameSecreto"
    PERIOD = 1000

    while not Lotengo:
        radio.config(power = POWBEACONSEC, group = ID)
        radio.send(SECRET_REQUEST)
        for i in range(5):
            received2 = radio.receive_full()
            if received2 != None:
                msgScr2, dBmScr2, _ = received2
                SECRET_MSG = str(msgScr2[6:], 'utf8')
                if SECRET_MSG != SECRET_REQUEST:
                    display.scroll('Sec:')
                    display.scroll(SECRET_MSG)
                    return SECRET_MSG
                    Lotengo = True
            sleep(PERIOD)

def Escucho_al_cocheJefe():
#El Coche-Esclavo se pone a escuchar que las ordenes que le asigna el Coche-Jefe
#Los codigos que puede recibir significan:
#'66666': indica que va a recibir a continuacion un ID de baliza nuevo, la cual tendra que localizar y sacar su secreto
#'99999': indica que es el Final y a continuacion el Coche-Jefe le va a enviar todas las balizas y sus secretos
#'88888': se usa para indicar que no tiene que ninguna baliza asignada
    radio.off()
    radio.on()
    POWBEACON = 7
    GRUPO = 40
    LONG = 128
    BALIZA_REQUEST = 'DamelaListadeBalizas'
    IDREQ = 'DameID'
    NEWIDCODE = 66666
    ID_FINAL = 99999
    ID_Bal = 88888
    PERIOD = 1000
    Baliz = ""              #Almacenará el string completo con todos los secretos
    Orden = 0
    Salgo = False
    Salgo2 = False
    radio.config(power = POWBEACON, group = GRUPO, length = LONG)
    RecibidaOrden = False

    while not RecibidaOrden:
        received = radio.receive_full()
        if received != None:
            msg, dBm, _ = received
            BEACON_Orden = str(msg[3:], 'utf8')
            if BEACON_Orden != "":
                Orden = int(BEACON_Orden)

            if Orden == ID_FINAL:            # Si es codigo recibido es '99999', recibiré a continuacion la cadena final de las Balizas y sus secretros
                display.show(Image.BUTTERFLY)
                ID_Bal = ID_FINAL
                for j in range(5):
                    radio.send(BALIZA_REQUEST)
                    while not Salgo:
                        received2 = radio.receive_full()
                        if received2 != None:
                            msgScr2, dBmScr2, _ = received2
                            Baliz = str(msgScr2[3:], 'utf8')
                            if Baliz != "" and Baliz != BEACON_Orden:
                                return ID_Bal, Baliz
                                Salgo = True
                        sleep(PERIOD)

            if Orden == NEWIDCODE:            # Si es codigo recibido es '66666', recibiré a continuacion un nuevo ID de baliza
                for j in range(5):
                    radio.send(IDREQ)
                    while not Salgo2:
                        received3 = radio.receive_full()
                        if received3 != None:
                            msgScr3, dBmScr3, _ = received3
                            ID_Bal = str(msgScr3[3:], 'utf8')
                            if ID_Bal != "" and ID_Bal != BEACON_Orden:
                                display.scroll('ID:')
                                display.scroll(ID_Bal)
                                return ID_Bal, Baliz
                                Salgo2 = True
                        sleep(PERIOD)
            RecibidaOrden = True
        sleep(PERIOD)
    return ID_Bal, Baliz

def Aviso_al_jefe(code):
#Uso esta funcion para avisar al Coche-Jefe cuando ya he conseguido el secreto de la baliza que me habian asignado
#El Coche-Esclavo envia el mensaje 'Ready?' en bucle hasta que el Coche-Jefe tambien le responda 'Ready?'
#A continuación, le enviará el secreto descubierto
    radio.off()
    radio.on()
    POWBEACON = 7
    GRUPO = 40
    PERIOD = 1000
    ID_READY = 'Ready?'
    LoTiene = False

    while not LoTiene:
        radio.config(power = POWBEACON, group = GRUPO)
        radio.send(ID_READY)
        display.scroll('Ready?')
        for i in range(5):
            received2 = radio.receive_full()
            if received2 != None:
                msgScr2, dBmScr2, _ = received2
                SECRET_MSG = str(msgScr2[3:], 'utf8')
                if SECRET_MSG == ID_READY:
                    for i in range(5):
                        radio.send(code)
                    LoTiene = True
            sleep(PERIOD)

def main():
#El programa pone al Coche-Esclavo en bucle de espera hasta recibir todas las Balizas y los secretos del Coche-Jefe
#Además tambien escucha al Coche-Jefe por si le asigna en algun momento un ID de baliza para buscar
#Si recibe un ID '66666' del Coche-Jefe, a continuacion recibe el ID de la nueva baliza a buscar
#Si recibe un ID '99999', se preparará para recibir a continuacion la cadena final de todos los IDs y secretos de las Balizas
#Si el ID es '88888', no hace nada

    radio.on()
    global Balizas
    Balizas = ""
    TengoBalizas = False
    ID_FINAL = 99999
    ID_VOID = 88888
    IDREQ = 66666
    STRING = "03:MiGrupo:lcrespo"
    Formateado = ""

    while not TengoBalizas:
        codigo = "a"
        CodigoEntregado = False
        Ordenes = Escucho_al_cocheJefe()  #Aqui escucha las ordenes del Coche-Jefe
        while not CodigoEntregado:        #y se pone en bucle hasta que no haya entregado su respuesta al Coche-Jefe
            ID_Bst, Balizas = Ordenes
            ID_B = int(ID_Bst)
            if Balizas != "":              #Si con las ordenes recibidas, me llega el String final de todas las balizas, salgo del bucle
                CodigoEntregado = True
                TengoBalizas = True
            if ID_B != ID_VOID and ID_B != ID_FINAL and ID_B != IDREQ:
                #Si con las ordenes del Coche-Jefe recibo un ID valido de baliza para buscar su secreto,
                #aquí iría moviendo el coche hasta acercarme lo suficiente a la baliza para poder leerlo
                #Pero al no tener espacio de memoria suficiente en el microbit para programar las funciones de movimiento, se ha obviado ese paso
                #Se asume que estamos cerca de la baliza y se intenta leer su secreto
                codigo = intercambio_secreto(ID_B)
                if codigo != "":
                    Aviso_al_jefe(codigo)   #Cuando ya tengo el secreto del ID que me han asignado, aviso al Coche-Jefe
                    ID_B = ID_VOID
                    CodigoEntregado = True
    #Cuando recibo el String completo de todos los IDs y sus secretos, los muestro por el display
    Formateado = Balizas
    StringFinal = STRING + Balizas
    display.scroll(StringFinal)

#AQUI CONTINUARIAMOS CON LA SEGUNDA PARTE DEL PROGRAMA, QUE ES LA QUE MUEVE LOS COCHES HASTA EL ARBITRO Y LE ENTREGA TODOS LOS IDS Y SUS SECRETOS
#LOS DOS COCHES USAN EL MISMO CODIGO PARA ESTA TAREA ("FASE3-2-Ir a meta + Arbitro-AmbosCoches")

if __name__ == "__main__":
    main()