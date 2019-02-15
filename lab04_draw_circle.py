import turtle

def drawShape(t, n, sz):
    """Make turtle t draw a shape with n-sides of equal lengths - sz."""
    turn_angle=360/n
    for i in range(n):
        t.forward(sz)
        t.left(turn_angle)

        
def drawSquare(t, sz):
    """Make turtle t draw a square of size sz."""
    drawShape(t, 4, sz)
    
wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           
#drawSquare(tess, 50)
drawShape(tess, 3, 50)

wn.exitonclick()
