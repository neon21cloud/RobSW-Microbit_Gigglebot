ladstr = input("int num de lados")
lad = int(ladstr)
polstr = input("int tamanho de lados")
pol = int(polstr)

import turtle
wn = turtle.Screen()
chus = turtle.Turtle()

chus.penup()
chus.goto(100,-100)
chus.down()
for _ in range(lad):
    chus.forward(pol)
    chus.right(360/lad)

chus.penup()
chus.goto(100,100)
chus.down()
for _ in range(lad):
    chus.forward(pol)
    chus.right(360/lad)

chus.penup()
chus.goto(-100,-100)
chus.down()
for _ in range(lad):
    chus.forward(pol)
    chus.right(360/lad)

chus.penup()
chus.goto(-100,100)
chus.down()
for _ in range(lad):
    chus.forward(pol)
    chus.right(360/lad)


wn.exitonclick()
