import re

def ile_liter(litera):
    suma = 0
    f = open("dane.txt", "r")
    a = f.read()
    c = re.findall("\b\w\b",a)
    print(c)
    
ile_liter(2)
    