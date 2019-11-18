import turtle

x = int(input("Podaj pierwszą współrzędną lewego górnego narożnika: "))
y = int(input("Podaj drugą współrzędną lewego górnego narożnika: "))
n = int(input("Podaj bok kwadratu: "))

def drawSquare(x,y,n):
    turtle.setposition(x,y)
    turtle.setheading(90)
    pen.forward(n)
    turtle.done()
    
print(drawSquare(x,y,n))
    