n = 0

def miesiąc(n):
    Miesiące = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopda", "Grudzień"]
    if n<0 and n>12:
        return "Podaj liczbe pomiędzy 1 a 12"
    else:
        return Miesiące[n-1]
miesiąc(n)


print(miesiąc(7))
print(miesiąc(9))
Array = [miesiąc(7), miesiąc(9)]
print("=========================")
print(Array)