Macierz = [[1,2,0],[0,0,3],[5,1,1]]

def transpozycja(Macierz):
    Macierz2 = [[],[],[]]
    x=-1
    for i in Macierz:
        for j in Macierz2:
            i.append(j[x])
        x+=1
    return Macierz2


print(transpozycja(Macierz))
                           
    

