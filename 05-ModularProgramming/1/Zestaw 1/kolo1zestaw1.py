# PP1 KOLOKWIUM 1 ZESTAW 1

# uzyskana liczba punktów
total = 0
print('WYKONANO POPRAWNIE')
print('------------------')

# zadanie 2 pkt
try:
    from zadanie2 import dodatek_stazowy
    if dodatek_stazowy(9) == 1150:
        total += 2
        print('zadanie za 2 pkt')
except:
    pass


# zadanie 4 pkt
try:
    from zadanie4 import suma_liczb
    if suma_liczb(5,10,3,4) == 23:
        total += 4
        print('zadanie za 4 pkt')
except:
    pass



# zadanie 6 pkt
try:
    from zadanie6 import slownie
    if slownie(347) == "trzy,cztery,siedem":
        total += 6
        print('zadanie za 6 pkt')
except:
    pass



# zadanie 8 pkt
try:
    from zadanie8 import bez_duplikatow
    if bez_duplikatow([7,2,4,2,1,7]) == 5:
        total += 8
        print('zadanie za 8 pkt')
except:
    pass



# zadanie 10 pkt
try:
    from zadanie10 import ile_liter
    if ile_liter("e") == 2:
        total += 10
        print('zadanie za 10 pkt')
except:
    pass


# końcowy rezultat
print('------------------')
print(f'RAZEM: {total} pkt')

