from microbit import *
import music
import radio

def main():

    radio.config(power=7, group=10)
    radio.on()
    while True:


        r = radio.receive_full()

        if r != None:
            msg, dBm, _ = r
            msg = str(msg[3:], 'utf8')

            if msg == 'dot':
                display.show(Image('00000:00000:00900:00000:00000'))
                # music.play('F5:1') #String que representa: F(Nota) 5(Octava) 3(Beats)
                sleep(150)
                display.clear()
                sleep(150)


            elif msg == 'dash':
                display.show(Image('00000:00000:99999:00000:00000'))
                # music.play('F5:3')
                sleep(150)
                display.clear()
                sleep(150)


if __name__ == "__main__":
    main()