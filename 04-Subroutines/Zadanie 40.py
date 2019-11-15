Tab = [1,2,3,4,5,6,7,8]

def anon(i):
    if i%2==0:
        return True
    else:
        return False
    

Parzyste = filter(anon, Tab)

for i in Parzyste:
    print(i)