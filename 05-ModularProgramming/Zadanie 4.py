import math
x = 3.7
y = 4

def PierwiastekKwadratowy(x):
    return math.sqrt(x)

def XdoY(x,y):
    return math.pow(x,y)

def polekoła(y):
    return f"{(math.pow(y,2)*2)}Pi"

def silnia(y):
    return math.factorial(y)

def NajwiekszaCal(x):
    return math.floor(x)


print(f"Pierwiastek kwadratowy z X: {PierwiastekKwadratowy(x)}")
print(f"X do potęgi Y: {XdoY(x,y)}")
print(f"Pole koła o promieniu Y: {polekoła(y)}")
print(f"Silnia Y: {silnia(y)}")
print(f"Najwieksza możliwa liczba całkowita <=x: {NajwiekszaCal(x)}")