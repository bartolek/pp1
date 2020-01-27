def suma_liczb(a,b,c,d):
    suma = 0
    for i in range(a,b+1):
        if i%c==0 or i%d==0:
            suma+=i
    return suma
            
        
