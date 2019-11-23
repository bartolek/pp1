import statistics as s
import csv

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    wiek = []
    i=0
    for row in reader:
        if i!=0:
            wiek.append(int(row[2]))
        elif i==0:
            i+=1

    
print(f"Średnia arytmetyczna wieku w firmie to: {s.mean(wiek)}")
print(f"Mediana wieku w firmie to: {s.median(wiek)}")
print(f"Odchylenie standartowe wieku pracowników wynosi: {s.stdev(wiek)}")
        