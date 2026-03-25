import turtle
def poligono (turtle,lad,pol):
    for _ in range (int(lad)):
        chus.forward(int(pol))
        chus.right(360/int(lad))

wn = turtle.Screen()
chus = turtle.Turtle()
ladstr = input("int num de lados")
polstr = input("int tamanho de lados")

chus.penup()
chus.goto(100,-100)
chus.down()
poligono(chus,ladstr,polstr)

chus.penup()
chus.goto(100,100)
chus.down()
poligono(chus,ladstr,polstr)

chus.penup()
chus.goto(-100,-100)
chus.down()
poligono(chus,ladstr,polstr)

chus.penup()
chus.goto(-100,100)
chus.down()
poligono(chus,ladstr,polstr)

wn.exitonclick()
