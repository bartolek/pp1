import random


def randomNumber():
    return random.randrange(1,51)
randomNumber()

parzyste = 0
nieparzyste = 0

for i in range(1,1001):
    if randomNumber()%2==0:
        parzyste+=1
    else:
        nieparzyste+=1
        
print("Dla 1000 liczb losowych z przedziału <1,50>:")
print(f"Liczby parzyste: {parzyste/10}%")
print(f"Liczby nieparzyste: {nieparzyste/10}%")
    