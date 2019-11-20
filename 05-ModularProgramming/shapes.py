import turtle

def drawSquare(x,y,n):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for i in range(0,4):
        turtle.right(90)
        turtle.forward(n)