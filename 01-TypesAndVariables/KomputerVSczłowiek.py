def KomputerVSczłowiek ():
    
    import random
    liczba1 = random.randrange(1,6)
    liczba2 = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
    print("==================================")
    print("Komputer wyrzucił: %s" % (liczba1))
    if liczba1 == liczba2:
        print("Zgadłeś: True")
    else:
        print("Zgadłeś: False")
    
    
    
KomputerVSczłowiek()