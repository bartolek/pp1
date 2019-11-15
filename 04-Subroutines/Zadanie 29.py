import statistics 

Tablica = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]


def mediana(Tablica):
    Tablica.sort()
    x = (len(Tablica)//2) 
    if x%2==0:
        mediana = (Tablica[x] + Tablica[x-1])/2
        return mediana
    mediana(Tablica)

def modalna(Tablica):
    return statistics.mode(Tablica)
modalna(Tablica)
    

print(f"Mediana: {mediana(Tablica)}")
print(f"Dominanta: {modalna(Tablica)}")

