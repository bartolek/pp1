def bez_duplikatow(tablica):
    suma = 0
    tab2 = []
    for i in range (len(tablica)):
        a = tablica[i]
        tablica[i] = "g"
        if a not in tablica:
            suma+= a
        tablica[i] = a
    return suma;
        
    
    