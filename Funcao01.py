import turtle
def DesenhaQuadradoColorido(tart,green):
    tart.begin_fill()
    tart.fillcolor(green)
    for jafiz in range(4):
        tart.fd(100)
        tart.rt(90)
    tart.end_fill()
    return
def DeslocaQuadrado(tart):
    tart.rt(45)
    tart.up()
    tart.fd(100)
    tart.lt(45)
t=turtle.Turtle()
t.reset()
t.left(45)
DesenhaQuadradoColorido(t,'green')
DeslocaQuadrado(t)
DesenhaQuadradoColorido(t,'yellow')
