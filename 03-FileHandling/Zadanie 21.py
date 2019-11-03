tab = []
suma = 0
with open("numbersinrows.txt", "r") as file:
    for line in file:
        x = line.split(",")
        for i in range(len(x)):
            tab.append(x[i])
            suma+=int(x[i])
print("Ilosc liczb to",len(tab))
print("Suma tych liczb to ", suma)