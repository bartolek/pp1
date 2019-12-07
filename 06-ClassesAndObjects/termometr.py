import random
class termometr():
    def __init__(self):
        self.is_on = False
        self.temperature = round(random.uniform(34,42),1)
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def info(self):
        if self.temperature>37 and self.temperature<41:
            print(f"Temperatura wynosi: {self.temperature} stopni(a), co oznacza gorączkę.")
        elif self.temperature>41:
            print(f"Temperatura wynosi: {self.temperature} stopni(a), STAN ZAGROŻENIA ŻYCIA!!!")
        else:
            print(f"Temperatura wynosi: {self.temperature} stopni(a).")
            