import re
suma = 0

with open("land.txt", "r") as file:
        string=file.read()
        numery = re.findall("\d[0-9]",string)
        for i in range(len(numery)):
            suma+=int(numery[i])
            
print(suma)
        