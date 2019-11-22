import turtle

def drawSquare(x,y,m):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for i in range(0,4):
        turtle.right(90)
        turtle.forward(m)
        
def drawTriangle(x,y,m):
    turtle.fillcolor("green")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(m)
        turtle.left(120)
    turtle.end_fill()
        
def drawCircle(x,y,n):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.circle(n)
    
def drawStar():
    for i in range(10):
        if i%2==0:
            turtle.left(72)
            turtle.forward(90)
        else:
            turtle.right(144)
            turtle.forward(90)
            
def drawCross(x,y,m):
    z = x
    turtle.speed(9999)
    for i in range(8):
        for j in range(8):
            if i%2==0:
                if j%2==0:
                    turtle.fillcolor("black")
                    turtle.begin_fill()
                    drawSquare(x,y,m)
                    turtle.end_fill()
                    x+=m
                elif j%2!=0:
                    drawSquare(x,y,m)
                    x+=m
            elif i%2!=0:
                if j%2==0:  
                    drawSquare(x,y,m)
                    x+=m
                elif j%2!=0:
                    turtle.fillcolor("black")
                    turtle.begin_fill()
                    drawSquare(x,y,m)
                    turtle.end_fill()
                    x+=m
        x=z
        y+=m


            
drawCross(-150,-150,50)
        



