liczba = 23
tablica = [15,38,7,23,14]

def występuje(liczba,tablica):
    for i in range(len(tablica)):
        if tablica[i] == liczba:
            print(f"Rezultat: Podana liczba wystepuje w tablicy")          
print(f"Liczba: {liczba}")
print(f"Tablica: {tablica}")
występuje(liczba,tablica)

