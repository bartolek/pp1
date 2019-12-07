from math import gcd
class ułamek():
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def ułamek(self):
        print(f"{self.licznik}/{self.mianownik}")
    def short(self):
        x = gcd(self.licznik,self.mianownik)
        self.licznik //= x
        self.mianownik //= x
    
        
        
ułamek = ułamek(20,5)
ułamek.ułamek()
ułamek.short()
ułamek.ułamek()