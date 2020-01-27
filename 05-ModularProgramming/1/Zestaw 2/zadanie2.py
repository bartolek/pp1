def ile_monet(kwota):
    suma = 0
    reszta = 0
    suma+= int(kwota/5)
    reszta= kwota%5
    suma+= int(reszta/2)
    reszta= reszta%2
    suma+= int(reszta/1)
    reszta = kwota%1
    return suma

    
ile_monet(18)