import random

def rzucKostka():
    x = random.randint(1,6)
    return x
rzucKostka()

suma = 0
for i in range(3):
    rzut = rzucKostka()
    suma+= rzut
    print(rzut)
print(f"Suma: {suma}")