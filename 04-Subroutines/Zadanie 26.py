dochod = int(input("Podaj dochód: "))

def podatek(dochod):
    podatek = 0
    if dochod<=5000:
        podatek = dochod*0.17
    elif dochod>5000:
        podatek1 = 5000*0.17
        dochod2 = dochod-5000
        podatek2 = dochod2*0.32
        podatek = podatek1 + podatek2
    return podatek

podatek(dochod)

print(f"Podatek należny: {podatek(dochod)}")