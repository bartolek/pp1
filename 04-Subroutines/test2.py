tablica = [1,2,3,4,5,6,7,8,9]

def suma_parzyste(tablica):
    suma = 0
    for i in range(len(tablica)):
        if tablica[i]%2==0:
            suma+=tablica[i]
    return suma

print(suma_parzyste(tablica))
            