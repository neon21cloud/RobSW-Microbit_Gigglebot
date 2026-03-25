ladstr = input("int num de lados")
lad = int(ladstr)
polstr = input("int tamanho de lados")
pol = int(polstr)


import turtle
wn = turtle.Screen()
chus = turtle.Turtle()

for _ in range(lad):
    chus.begin_fill
    chus.forward(pol)
    chus.right(360/lad)
    chus.end_fill

wn.exitonclick()
