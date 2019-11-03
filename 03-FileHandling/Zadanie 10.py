with open('C:/Users/Barteklaptop/Desktop/pp1/03-FileHandling/Numbers.txt','r') as file:
    suma = 0
    for line in file:
        suma +=int(line)
    print(suma)
        
