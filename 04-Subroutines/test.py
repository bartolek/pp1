Tab = [9,2,7,4,5,6,7,8,9]
Tab2 = [3,5,9]

def inne_liczby(Tab,Tab2):
    inne = []
    suma = 0
    suma2 = 0
    suma3 = 0
    suma = 0
    for i in range(len(Tab)):
        for j in range(len(Tab2)):
            if Tab[i]==Tab2[j]:
                inne.append(Tab[i])
                
    for a in range(len(inne)):
        suma+=inne[a]
    for z in range(len(Tab)):
        suma2+=Tab[z]
   
    return suma2-suma


print(inne_liczby(Tab,Tab2))
                