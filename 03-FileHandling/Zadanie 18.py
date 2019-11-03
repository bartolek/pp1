liczby = []

with open("numbers.txt", "r") as file:
    for line in file:
        liczby.append(int(line))
liczby.sort()
print(liczby)

    