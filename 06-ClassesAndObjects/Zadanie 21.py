from statistics import mean,median
class statystyka():
    def __init__(self, ciąg):
        self.ciąg = ciąg
    def add(self,added):
        self.ciąg.append(added)
    def space(self):
        s = ""
        for i in self.ciąg:
            s+=str(i)+ " "
        print(s)
    def max(self):
        max = self.ciąg[0]
        for i in self.ciąg:
            if i>max:
                max = i
        print(f"Największa liczba w tym ciągu to: {max}")
    def min(self):
        min = self.ciąg[0]
        for i in self.ciąg:
            if i<min:
                min = i
        print(f"Najmniejsza liczba w tym ciągu to: {min}")
    def mean(self):
        print(f"Średnia arytmetyczna ciągu to: {mean(self.ciąg)}")
    def median(self):
        print(f"Mediana tego ciągu to: {median(self.ciąg)}")
        
s = statystyka([12,37,6,9])
s.add(17)
s.space()
s.max()
s.min()
s.mean()
s.median()