import turtle
wnd = turtle.Screen()

elan = turtle.Turtle()

distance = 50
elan.right(30)
for _ in range(23):
    elan.forward(distance)
    elan.right(120)
    distance = distance + 10

wnd.exitonclick()
