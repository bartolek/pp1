with open("ShoppingList.txt", "w") as file:
    x = input("Dodaj produkt: ")
    while len(x)!=0:
        file.write(x + '\n')
        x = input("Dodaj produkt: ")
file.close()
    