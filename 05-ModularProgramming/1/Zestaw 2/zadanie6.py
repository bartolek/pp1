def symbole(liczba):
    wynik = ""
    sum = 0
    for i in str(liczba):
        wynik+= "*"*int(i)
        sum+=1
        if sum < len(str(liczba)):
            wynik+= ","
    return wynik
    
    

    