def suma_duplikatow(tablica):
    suma = 0
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            a = tablica[i]
            tablica[i] = "f"
            print(a)
            if tablica[j] == a:
                tablica[j]= "f"
                print(tablica)
                break
                
            

        
    
    
suma_duplikatow([2,3,4,2,5,3,3])