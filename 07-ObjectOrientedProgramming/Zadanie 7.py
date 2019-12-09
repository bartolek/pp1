class Student():
    
    Uczelnia = "Uek Kraków"
    Numer = 100000
    
    def __init__(self, imie, nazwisko, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        Student.Numer+=1
        self.nralbumu = Student.Numer
        self.kierunek = kierunek
    def __str__(self):
        return f"{self.imie} {self.nazwisko.upper()} ({self.nralbumu}), {self.kierunek}, {Student.Uczelnia}"
    
print(Student("Wacław", "Potocki", "Informatyka Stosowana"))
print(Student("Jan", "Kowalczyk", "Ekonometria"))
print(Student("Kamila", "Synowiecka", "Ekonomia"))
print(Student("Agata", "Korzeń", "Informatyka i ekonometria"))