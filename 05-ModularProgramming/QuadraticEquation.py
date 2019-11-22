
def czytajWspolczynniki():
    print("Wpisz współczynniki wzoru: ax+bx+c=0")
    a = int(input("Wczytaj współczynnik a: "))
    b = int(input("Wczytaj współczynnik b: "))
    c = int(input("Wczytaj współczynnik c: "))
    return [a,b,c]

def obliczDelte(wspolczynniki):
    return (wspolczynniki[1]**2)-(4*wspolczynniki[0]*wspolczynniki[2])


def obliczPierwiastki(wspolczynniki):
    from math import sqrt
    delta = obliczDelte(wspolczynniki)
    if delta>0:
        x1 = ((-1)*wspolczynniki[1]-sqrt(delta))/(2*wspolczynniki[0])
        x2 = ((-1)*wspolczynniki[1]+sqrt(delta))/(2*wspolczynniki[0])
        Pierwiastki = [x1,x2]
        return Pierwiastki 
    elif delta == 0:
        x1 = (-wspolczynniki[1]/2*wspolczynniki[0])
        Pierwiastki = [x1]
        return Pierwiastki 
    elif delta < 0:
        Pierwiastki = []
        return Pierwiastki 
    
def wyswietlPierwiastki(wynik_rownania):
    return print(f"Pierwiastki tego rownania to: {wynik_rownania[0]}, {wynik_rownania[1]}")
        