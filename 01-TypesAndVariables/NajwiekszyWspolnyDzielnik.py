def NajwiekszyWspolnyDzielnik ():
    
    import math
    liczba1 = int(input("Podaj pierwszą liczbę naturalną: "))
    liczba2 = int(input("Podaj drugą liczbę naturalną: "))
    print("Największym wspólnym dzielnikiem jest liczba: ", math.gcd(liczba1,liczba2))
    
NajwiekszyWspolnyDzielnik()