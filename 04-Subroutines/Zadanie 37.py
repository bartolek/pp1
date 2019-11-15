tab = [1,2,3,4,5,1,1,1,1,1]

def onlyonce(tab):
    return {i for i in tab if tab.count(i)<2}
        
print(onlyonce(tab))
        

