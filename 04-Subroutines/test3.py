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
            
import csv
import statistics 
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            print(f"X  {row[0].upper()}  {row[1].upper()}  {row[2].upper()}  {row[3].upper()}")
            print("="*60)
            i+=1
        
    