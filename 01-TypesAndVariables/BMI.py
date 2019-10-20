def BMI ():
    wzrost = float(input("Podaj wzrost w cm: "))
    waga = float(input("Podaj wagę w kg: "))
    print("Wskaźnik BMI: ", round( waga / (wzrost*wzrost)*10000, 2))



BMI()
