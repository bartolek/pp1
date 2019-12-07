class kontakt():
    def __init__(self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon
    def back(self):
        return f"{self.nazwa}  {self.email}  {self.telefon}"
        
        
class ListaKontaktow():
    def __init__(self):
        self.kontakty = []
    def dodaj(self, dodaj):
        self.kontakty.append(dodaj)
    def show(self):
        print(self.kontakty)
        
        
k = kontakt("Kowalski Jan", "jank@onet.pl", 555234000)
l = ListaKontaktow()
l.dodaj(k.back())
l.show()
k = kontakt("Kowalski Paweł", "Paweł@onet.pl", 222222222)
l.dodaj(k.back())
l.show()