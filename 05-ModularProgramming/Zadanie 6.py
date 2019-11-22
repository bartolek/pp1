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

        else:
            print(f"{i} {row[0]}  {row[1]}  {row[2]}  {row[3]}")
            i+=1
    print("="*60)
    
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    wiek = []
    a = 0
    for row in reader:
        if a!=0:
            wiek.append(int(row[2]))
        a+=1
    print(f"Średni wiek: {statistics.mean(wiek)}")
        

