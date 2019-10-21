x = int(input("Podaj wiek psa w ludzkich latach: "))
    
if x<=2:
    print("Wiek psa w psich latach to: %s" % (x*10.5))
if x>2:
    print("Wiek psa w psich latach to: %s" % (21+x*4-8))
if x<0:
    print("Wiek psa nie może wynosić mniej niż 1")
        