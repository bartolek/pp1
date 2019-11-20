
def czytajWspolczynniki(a,b,c):
    return [a,b,c]

def obliczDelte(a,b,c):
    return (b**2+4*a*c)/2


def obliczPierwiastki(a,b,c):
    delta = 0
    delta = (b**2)-(4*a*c)
    if delta>0:
        x1 = (delta-b/2*a)
        x2 = (delta+b/2*a)
        Pierwiastki = [x1,x2]
        return print(Pierwiastki) 
    elif delta == 0:
        x1 = (-b/2*a)
        Pierwiastki = [x1]
        return Pierwiastki 
    elif delta < 0:
        Pierwiastki = []
        return Pierwiastki 
    
def wyswietlPierwiastki(x1,x2):
        return print(x1,x2)
        