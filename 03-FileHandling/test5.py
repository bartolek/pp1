import random

def losowa():
    return random.randint(1,51)

parzyste = 0
nieparzyste = 0

for i in range(1,1001):
    x = losowa()
    if x%2==0:
        parzyste+=1
    else:
        nieparzyste+=1
        
print(f"Parzystych jest: {parzyste/10}%")
print(f"Nieparzystych jest: {nieparzyste/10}%")