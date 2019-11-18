import random
import re

    random.randint(1,4)
    komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
    cyfry = re.findall('\d{2}',komunikat)
    suma = 0
    
    with open("numbers.txt", "r") as file:
    for line in file:
        liczby.append(int(line))
        
    import re
    suma = 0

    with open("land.txt", "r") as file:
        string=file.read()
        numery = re.findall("\d",string)
        for i in range(len(numery)):
            suma+=int(numery[i])
        
    