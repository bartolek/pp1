def slownie(liczba):
    wynik = ""
    sum = 0
    array = ["jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
    for i in str(liczba):
        wynik+= array[int(i)-1]
        sum+=1
        if sum < (len(str(liczba))):
            wynik+=","
    return wynik
    
    