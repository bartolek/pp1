import turtle

x = int(input("Podaj pierwszą współrzędną lewego górnego narożnika: "))
y = int(input("Podaj drugą współrzędną lewego górnego narożnika: "))
n = int(input("Podaj bok kwadratu: "))

def drawSquare(x,y,n):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for i in range(0,4):
        turtle.right(90)
        turtle.forward(n)
        
poziom = [x,x+n,x+2*n,x+3*n]
pion = [y,y-n,y-2*n,y-3*n]
for i in range(0,4):
    for j in range(0,4):
        drawSquare(poziom[j],pion[i],n)
    
    

    

