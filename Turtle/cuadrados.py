import turtle

def poligono (turtle,num,tam,ang):
    for _ in range (int(num)):
        chus.left(int(ang))
        for _ in range (4):
            chus.forward(int(tam))
            chus.right(90)

wn = turtle.Screen()
chus = turtle.Turtle()
numstr = input("int num de cuadrados")
tamstr = input("int tamanho de lados")
angstr = input("int tamanho de angulos")

poligono (chus,numstr,tamstr,angstr)

wn.exitonclick()
