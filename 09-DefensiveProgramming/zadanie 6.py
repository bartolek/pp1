print("a/b = xx")
a = input("Podaj a: ")
b = input("Podaj b: ")
assert type(a) != int, "Podaj liczbe"
print(f"{a}/{b} = {a/b}")