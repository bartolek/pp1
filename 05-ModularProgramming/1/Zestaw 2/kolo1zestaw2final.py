# PP1 KOLOKWIUM 1 ZESTAW 1

# uzyskana liczba punktów
total = 0
print('WYKONANO POPRAWNIE')
print('------------------')

# zadanie 2 pkt
try:
    from zadanie2 import ile_monet
    if ile_monet(17) == 4:
        total += 2
        print('zadanie za 2 pkt')
except:
    pass


# zadanie 4 pkt
try:
    from zadanie4 import ile_liczb
    if ile_liczb(5,12,3,4) == 4:
        total += 4
        print('zadanie za 4 pkt')
except:
    pass



# zadanie 6 pkt
try:
    from zadanie6 import symbole
    if symbole(3472) == "***,****,*******,**":
        total += 6
        print('zadanie za 6 pkt')
except:
    pass



# zadanie 8 pkt
try:
    from zadanie8 import suma_duplikatow
    if suma_duplikatow([2,3,4,2,5,3,3]) == 13:
        total += 8
        print('zadanie za 8 pkt')
except:
    pass



# zadanie 10 pkt
try:
    from zadanie10 import ile_cyfr
    if ile_cyfr("1") == 1:
        total += 10
        print('zadanie za 10 pkt')
except:
    pass


# końcowy rezultat
print('------------------')
print(f'RAZEM: {total} pkt')

