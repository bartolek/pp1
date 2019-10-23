a = int(input("Podaj zmienna a: "))
b = int(input("Podaj zmienna b: "))
    
if b<0 and a<0:
    print("Obie zmienne a i b, posiadające wartości %s i %s są ujemne." % (a,b))
elif b>0 and a>0:
    print("Obie zmienne a i b, posiadające wartości %s i %s są dodatnie." % (a,b))
elif a<0:
    print("Zmienna a wynosząca %s posiada wartość ujemną." % (a))
elif b<0:
    print("Zmienna b wynosząca %s posiada wartość ujemną." % (b))