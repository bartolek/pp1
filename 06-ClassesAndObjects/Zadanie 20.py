class lot():
    def __init__(self, flightNumber):
        self.flightNumber = flightNumber
        self.flightAttitude = 0
        
    def take_off(self):
        self.flightAttitude = 1500
    def Change_attitude(self, attitude):
        if attitude<11000 and attitude>300:
            self.flightAttitude = attitude
        elif self.flightAttitude>200:
            self.flightAttitude = attitude
            print("UWAGA! Niebezpieczna zmiana wysokosci lotu!")
    def landing(self):
        if self.flightAttitude<500:
            print("Rozpoczynam procedure lądowania")
            self.flightAttitude = 0
        else:
            print("UWAGA! Zmieniasz wysokość lotu Obniż lot.")
    def info(self):
        print(f"Tu {self.flightNumber}, moja wysokość lotu to {self.flightAttitude}m")
            
            
lot = lot("LOT881")
lot.take_off()
lot.info()
lot.Change_attitude(8900)
lot.info()
lot.Change_attitude(200)
lot.info()
lot.landing()
lot.info()

