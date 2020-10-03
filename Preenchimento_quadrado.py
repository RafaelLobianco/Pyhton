import turtle
def DesenhaQuadrado (tart) :
    for jafiz in range(4):
        tart.fd(100)
        tart.rt(90)
    return
t = turtle.Turtle()
t.reset()
t.begin_fill()
t.fillcolor('green')
t.left(45)
DesenhaQuadrado(t)
t.end_fill()
t.right(45)
t.up()
t.fd(100)
t.down()
t.fillcolor('yellow')
t.begin_fill()
t.left(45)
DesenhaQuadrado(t)
t.end_fill()
