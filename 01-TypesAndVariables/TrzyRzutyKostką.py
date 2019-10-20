def TrzyRzutyKostką ():
    
    import random
    liczba1 = random.randrange(1,6)
    print("Pierwszy rzut kostką wylosował liczbę: %s" % (liczba1))
    liczba2 = random.randrange(1,6)
    print("Drugi rzut kostką wylosował liczbę: %s" % (liczba2))
    liczba3 = random.randrange(1,6)
    print("Trzeci rzut kostką wylosował liczbę: %s" % (liczba3))
    print("=========================================")
    print("Suma wyrzuconych oczek wynosi: %s" % (liczba1+liczba2+liczba3))
    
TrzyRzutyKostką()