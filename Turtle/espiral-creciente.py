'''Escribe un programa en Python llamado espiral-creciente.py en el que se dibuje una espiral formada por unos 800 trazos
rectilíneos, cada vez más largos y con el trazo cada vez más grueso. Para ello, el programa preguntará al usuario el incremento de
longitud y el ángulo que debe irse adoptando antes de dibujar cada nuevo trazo de la espiral. Cada nuevo trazo además debe dibujarse
con un lapicero de mayor grosor. Puedes hacer que el grosor se incremente levemente (por ejemplo 0.03) para cada trazo.
Pistas:
alex.pensize()
alex.pensize(5)
devuelve el valor actual del grosor del lapicero.
hace que el valor del grosor del lapicero pase a ser 5'''


import turtle

size=1
wn = turtle.Screen()
chus = turtle.Turtle()
tamstr = input("int tamanho que creceran los lados")
angstr = input("int tamanho de angulos")

def poligono(chus, tam, ang, calabacin):
    patata = 20       # empieza con un largo
    incremento = int(tam)
    giro = int(ang)
    for _ in range(800):
        patata += incremento
        chus.forward(patata)
        chus.right(giro)
        chus.pensize(calabacin)
        calabacin += 0.05


poligono (chus,tamstr,angstr,size)

wn.exitonclick()



