x = int(input("Podaj dolną liczbę zakresu: "))
y = int(input("Podaj dgórną liczbę zakresu: "))
z = int(input("Podaj liczbe do sprawdzenia: "))

def wprzedziale(x,y,z):
    if z > x and z < y:
        return "Liczba mieści się w zakresie"
    else:
        return "Liczba nie mieści się w zakrecie"
    
print(wprzedziale(x,y,z))
    
    
    