Tab = [32, 16, 5, 8, 24, 7]

with open("Tablica.txt", "w") as file:
    for i in range(len(Tab)):
        file.write(str(Tab[i]) + '\n')