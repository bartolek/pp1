class rachunek():
    def __init__(self, AccountNumber):
        self.AccountBalance = 0
        self.AccountNumber = AccountNumber
    def income(self, amount):
        self.AccountBalance+=amount
    def outcome(self, amount):
        if amount>self.AccountBalance:
            print("Niewystarczająca ilość środków na rachunku do wypłaty.")
        else:
            self.AccountBalance-=amount
    def showStatus(self):
        print(f"Rachunek nr: {self.AccountNumber} \nSaldo: {self.AccountBalance} PLN")
        
r = rachunek("12 3456 5555 9090 1111 0000 7722")
r.showStatus()
r.income(25.3)
r.showStatus()
r.outcome(31.7)
r.showStatus()
r.outcome(14)
r.showStatus()
        
    