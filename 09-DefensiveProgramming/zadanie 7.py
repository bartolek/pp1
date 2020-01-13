wzrost = int(input("Podaj wzrost w cm: "))
assert 150<wzrost<220, "Podaj wzrost między 150cm, a 220cm."
waga = float(input("Podaj wage w kg: "))
assert 40.0<waga<150.0, "Podaj wage między 40kg, a 150kg."
print(f"Twoje BMI to: {round(waga/((wzrost/100.0)*(wzrost/100.0)),2)}")