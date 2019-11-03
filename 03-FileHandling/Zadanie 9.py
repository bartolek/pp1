with open('C:/Users/Barteklaptop/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    i = 1
    for line in file:
        print(i, line, end='')
        i+=1
file.close()
