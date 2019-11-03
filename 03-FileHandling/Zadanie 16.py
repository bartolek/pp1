import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma = 0

for i in range(len(cyfry)):
    suma+=int(cyfry[i])
print("Średnia prognozowana temperatura przez najbliższe", len(cyfry),"dni wynosi: ",suma/len(cyfry))
    