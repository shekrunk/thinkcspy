import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.left(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

def drawFilledCircle(anyTurtle, radius, fill_color):
    anyTurtle.fillcolor(fill_color)
    anyTurtle.begin_fill()
    drawCircle(anyTurtle, radius)
    anyTurtle.end_fill()

wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 35)
drawFilledCircle(wheel, 50, "blue")

wn.exitonclick()
