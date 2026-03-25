petstr = input("int num de petalos")
pet = int(petstr)
import random

import turtle
wn = turtle.Screen()
cami = turtle.Turtle()

for _ in range(pet):
    cami.down()
    cami.circle(100,90)
    cami.left(90)
    cami.circle(100,90)
    cami.penup()
    cami.goto(random.randrange(1,500),random.randrange(10,100))

wnd.exitonclick()
