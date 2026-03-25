#Primera parte de la fase tres. Se trata de un esfuerzo de busqueda en equipo para DOS COCHES. Se asignan dos roles: Jefe y Esclavo.
#El Jefe es el único que busca nuevas balizas y se las reparte entre los dos para buscar secretos.

#Este es el programa del del Coche-Jefe.
#Dada la limitación de memoria, el programa solo contempla la comunicación que tiene lugar entre los dos gigglebots y omite las partes de movimiento.
#aunque esta estructurado de tal manera que de haber más memoria pudiese implementarse el movimiento sin otras modificaciones.
#Asume que puede hablar con las balizas desde cualquier punto de la habitación.

from microbit import *
import radio

def intercambio_secreto(ID):
#Misma rutina usada en la Fase2 para hablar con las balizas.
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
            received = radio.receive_full()
            if received != None:
                msgScr, dBmScr, _ = received
                SECRET_MSG = str(msgScr[6:], 'utf8')
                if SECRET_MSG != SECRET_REQUEST:
                    display.scroll('Sec:')
                    display.scroll(SECRET_MSG)
                    return SECRET_MSG
                    Lotengo = True
            sleep(PERIOD)

def Escucho_coche_esclavo():
#Uso esta funcion para escuchar al Coche-Esclavo cuando ya ha conseguido el secreto de la baliza que le he asignado
#El Coche-Esclavo envia el mensaje 'Ready?' en bucle hasta que el Coche-Jefe tambien responde 'Ready?'
#Y a continuación, se recibe el secreto descubierto por el Coche-Esclavo.
    radio.off()
    radio.on()
    POWBEACON = 7
    GRUPO = 40
    PERIOD = 1000
    codigo = ""
    IDINTERC = 'Ready?'
    Ready = False

    radio.config(power = POWBEACON, group = GRUPO)
    for i in range(5):
        received2 = radio.receive_full()
        if received2 != None:
            msgScr2, dBmScr2, _ = received2
            code = str(msgScr2[3:], 'utf8')
            if code == IDINTERC:                    #Si el Coche-Esclavo ha dicho 'Ready?',
                while not Ready:
                    radio.send(IDINTERC)            #le envio yo (Jefe) tambien para comfirmar un 'Ready?'
                    for i in range(5):
                        received3 = radio.receive_full()
                        if received3 != None:
                            msgScr3, dBmScr3, _ = received3
                            codigo = str(msgScr3[3:], 'utf8')           #y el Coche-Esclavo me devuelve el secreto que haya encontrado
                            if codigo != IDINTERC and codigo != "":
                                return codigo
                                Ready = True
                        sleep(PERIOD)
        sleep(PERIOD)

def Coordinador(ParaQuien):
# La funcion coordinador BUSCA BALIZAS NUEVAS y LAS REPARTE entre los dos coches.
# Devuelve el ID y su Posicion en la matriz global Balizas a main() para mantener un registro, siempre.
# Además, en caso de que se haya llamado al coordinador con un 1 (ParaQuien=1), el coordinador enviará el ID a Doy_Orden_al_coche_esclavo()
    radio.off()
    radio.on()
    POWBEACON = 7
    GRUPO = 41
    radio.config(power = POWBEACON, group = GRUPO)
    yaesta = 0
    metido = 0
    IDAsignado = 0
    Pos = 88888         #88888 es una manera simbolica de indicar que no hay una posicion asignada en la matriz Balizas.
    PERIOD = 1000
    MAX = 5
    IDAceptada = True

    for i in range(5):
        received4 = radio.receive_full()        #Busco un ID y compruebo si ya lo he encontrado antes o no
        if received4 != None:
            msg4, dBm4, _ = received4
            ID_BStr = str(msg4[6:], 'utf8')
            ID_B = int(ID_BStr)
            for i in range(MAX):
                if ID_B == Balizas[i][0]:
                    yaesta = 1
            for i in range(MAX):                #Si el ID es nuevo (yaesta), la posicion de la matriz donde la quiero guardar está libre y no está metida aun,
                if Balizas[i][0] == 0 and metido == 0 and yaesta == 0:
                    if ParaQuien == 1:          #Si está destinado para el esclavo, INTENTO asignarselo. Si lo consigo, IDAceptada == True
                        IDAceptada = Doy_Orden_al_coche_esclavo(ID_BStr)
                    if IDAceptada == True:      #Como por defecto IDAceptada == True, voy a entrar en este camino sea para quien sea. Pero si el esclavo no responde (o no lo acepta) quiere decir que no existe o está ocupado.
                        Balizas[i] = [ID_B, 0]
                        metido = 1
                        IDAsignado = ID_B
                        Pos = i
                        return Pos, IDAsignado
                    else:
                        return Pos, IDAsignado  #En caso de que el Esclavo no exista o acepte, los IDs detectados no sean nuevos, no guardo el ID ni su posición porque NO ESTAN ASIGNADOS.
        sleep(PERIOD)                           #En ese caso devuelvo los valores iniciales de Pos = 88888 y IDAsignado = 0
    return Pos, IDAsignado

def Doy_Orden_al_coche_esclavo(ID):
#Con esta funcion el Coche-jefe da ordenes al Coche-Esclavo.
#O bien le asigna un ID o bien le envía la matriz Balizas cuando ya está completa.
#Los codigos significan:
#'66666': indica al Coche-Esclavo que va a recibir a continuacion un ID de baliza para que busque su secreto
#'99999': indica al Coche-Esclavo que es el Final y a continuacion se van a enviar todas las balizas y sus secretos

    radio.off()
    radio.on()
    POWBEACON = 7
    GRUPO = 40
    PERIOD = 1000
    LONG = 128
    NEWIDCODE = '66666'
    ID_FINAL = '99999'
    IDREQ = 'DameID'
    BALIZA_REQUEST = 'DamelaListadeBalizas'
    IDAceptada = False

    #Por defecto, la baliza puede enviar datos de maximo 32bytes.
    #La he subido a 128bytes por si los codigos secretos son muy largos pero sin llegar al max de 251bytes para no agotar la memoria
    radio.config(power = POWBEACON, group = GRUPO, length = LONG)
    display.scroll('IDEsc:')
    display.scroll(ID)
    if ID == ID_FINAL:
        Enviar = ID_FINAL
    else:
        Enviar = NEWIDCODE
    for i in range(5):
        radio.send(Enviar)
    for i in range(5):                  #Si envio un 66666 o un 99999, el me devuelve lo mismo. Es una confirmacion para saber que esta escuchando.
        received5 = radio.receive_full()
        if received5 != None:
            msgScr5, dBmScr5, _ = received5
            respuesta = str(msgScr5[3:], 'utf8')
            if respuesta == IDREQ:      #Cuando confirmo que está escuchando, le envio su ID o la baliza global completa final con el formato que espera el arbitro: Formateado()
                dato = ID
            if respuesta == BALIZA_REQUEST:
                dato = Formateado
            for i in range(5):          #Si se ha enviado todo bien se devuelve IDAceptada = True. Si no, se devuelve IDAceptada = False por defecto
                radio.send(dato)
            IDAceptada = True
        sleep(PERIOD)
    return IDAceptada


def CambioFormato():
#Esta funcion se usa para cambiar a string el formato de la matriz de IDs de Balizas y sus secretos
    String = ''
    for t in range(len(Balizas)):
        if Balizas[t][0] != 0:
            String = String + "," + str(Balizas[t][0]) + ":" + str(Balizas[t][1])
    return String

def main():

    global Balizas
    global Formateado
    MAX = 5
    Balizas = [[0, 0]] * MAX
    Intentoslec = 0
    Estantodas = False
    Secreto = ""
    Formateado = ""
    StringFinal = ""
    CAB = '03:MiGrupo:lcrespo'
    POSINI = 88888
    ID_FINAL = '99999'
    PosMia = POSINI     #Posicion dentro de la matriz de Balizas del ID asignado al Jefe
    PosEsc = POSINI     #Posicion dentro de la matriz de Balizas del ID asignado al Esclavo
    ID_mio = 0
    IDAceptada = True

    while not Estantodas:

        #Si el esclavo tiene una Posicion de baliza asignada, le escucho a ver si encontró el Secreto
        if PosEsc != POSINI:
            Secreto = Escucho_coche_esclavo()
            if Secreto != "" and Secreto != None:   #Si lo encuentra lo muestro, lo guardo y le pongo la posición por defecto de 88888 (que indica no tener nada asignado)
                Balizas[PosEsc][1] = Secreto
                display.show('SecEsc:')
                display.scroll(Secreto)
                PosEsc = POSINI
        else:
            Inst = Coordinador(1)   #Si el esclavo no tiene nada asignado, llamo al Coordinador para que busque un ID para que se lo intente asignar
            PosEsc, ID_esc = Inst

        #Si el Jefe tiene una Posicion de baliza asignada, me comunico con ella para sacar su secreto
        if PosMia != POSINI and ID_mio != 0:
            #Aqui introduciria las rutinas de mover el coche hacia la baliza de forma identica a como se hizo en la Fase2
            #pero no estan porque no caben en memoria
            #El coche llamaria a la funcion de calculo de la Potencia Media de la baliza que busco y si la baliza esta en rango, leería el secreto
            #Si no está en rango, moveria el coche
            #PotMed = MidePotencia(ID_mio)
            #    if PotMed >= POTMINHABLARBALIZA:
            #        codigo = intercambio_secreto(ID_mio)
            #        if codigo != "" and codigo != None:
            #            Balizas[PosMia][1] = codigo
            #            PosMia = POSINI
            #    else:
            #        muevo_coche(PotMed, media_anterior)
            #        media_anterior = PotMed

            codigo = intercambio_secreto(ID_mio)
            if codigo != "" and codigo != None:
                Balizas[PosMia][1] = codigo
                #display.show('SecMio:')
                #display.scroll(codigo)
                PosMia = POSINI
        else:    #Si el Jefe no tiene nada asignado, llamo al Coordinador para que busque un ID para que se lo intente asignar
            Inst = Coordinador(0)
            PosMia, ID_mio = Inst
            if ID_mio != 0:
                display.show('MiID:')
                display.scroll(ID_mio)
            else:
                display.show('ID?')
                display.show(Image.CONFUSED)

#Cuando ni el Coche-Esclavo ni el Coche-Jefe tienen IDs pendientes de buscar y ya ha intentado buscar nuevas balizas 2*MAX veces, termina la busqueda.
        Intentoslec = Intentoslec + 1
        if Intentoslec > 2*MAX and PosMia == POSINI and PosEsc == POSINI:
            Estantodas = True

#Cambio a string el formato de la matriz de IDs de Balizas y sus secretos
    String = CambioFormato()
    Formateado = String
    StringFinal = CAB + String

#Si hay coche esclavo, le envío el string de IDs de Balizas y sus secretos
    IDAceptada = Doy_Orden_al_coche_esclavo(ID_FINAL)
    if IDAceptada == True:
        display.scroll('Enviando:')
    display.scroll(StringFinal)

#AQUI CONTINUARIAMOS CON LA SEGUNDA PARTE DEL PROGRAMA, QUE ES LA QUE MUEVE LOS COCHES HASTA EL ARBITRO Y LE ENTREGA TODOS LOS IDS Y SUS SECRETOS
#LOS DOS COCHES USAN EL MISMO CODIGO PARA ESTA TAREA ("FASE3-2-Ir a meta + Arbitro-AmbosCoches")

if __name__ == "__main__":
    main()