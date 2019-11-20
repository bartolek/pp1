import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)