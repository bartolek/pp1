def count(n):
    if n > 0 and n < 9:
        return 1
    else:
        return 1 + count(n//10)
    
print(count(int(input("Podaj liczbe: "))))