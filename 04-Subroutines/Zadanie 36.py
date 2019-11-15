tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]


def isinstancek(tab):
    total = 0
    for i in tab:
        if isinstance(i,list):
            total+= isinstancek(i)
        else:
            total+=i
    return total
    
print(isinstancek(tab))

