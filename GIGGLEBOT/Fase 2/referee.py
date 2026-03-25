import radio
from microbit import display, sleep

PREFIX_REQUEST  = "03:"
PREFIX_REPLY    = "04:"
GROUP_REFEREE   = 43
POWER_REFEREE   = 0
PERIOD         = 1000


def process(msg):
    login = None
    if len(msg) > 3:
        id_msg = msg[0:3]
        tail = msg[3:]
        if id_msg == PREFIX_REQUEST:
            login = tail.split(",")[0]

    return login


def main():

    radio.on()
    radio.config(power=POWER_REFEREE, group=GROUP_REFEREE, length = 128)
    #radio.config(power=POWER_REFEREE, group=GROUP_REFEREE)

    while True:
        display.clear()
        received = radio.receive_full()
        if received != None:
            msg, dBm, _ = received
            msg = str(msg[3:], 'utf8')
            login = process(msg)
            if login != None:
                # recibido mensaje correcto
                display.scroll(login, delay=50)
                radio.send(PREFIX_REPLY + login)
            else:
                # recibido mensaje incorrecto
                display.show("x")
        else:
            # no recibido nada
            display.show("-")
        sleep(PERIOD)


if __name__ == "__main__":
    main()