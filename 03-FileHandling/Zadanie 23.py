import re
suma = 0

with open("land.txt", "r") as file:
        string=file.read()
        numery = re.findall("\d",string)
        for i in range(len(numery)):
            suma+=int(numery[i])
            
print(suma)
        