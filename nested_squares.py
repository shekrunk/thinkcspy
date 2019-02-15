import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)

for i in range(5):
    print(20+(2*20*i))
    drawSquare(alex, 20+(2*20*i))   # Call the function to draw the square
    alex.penup()
    alex.goto(alex.xcor()-20, alex.ycor()-20)   # move alex to the starting position for the next square
    alex.pendown()

wn.exitonclick()

