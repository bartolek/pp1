suma_parzyste = 0
suma_nieparzyste = 0

for i in range(0,51):
    if i%2==0:
        suma_parzyste+=i
    elif i%2!=0:
        suma_nieparzyste+=i
        
print("Suma liczb nieparzystych z przedziału 1 do 50 wynosi %s" % (suma_nieparzyste))
print("Suma liczb parzystych z przedziału 1 do 50 wynosi %s" % (suma_parzyste))