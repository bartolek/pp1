from math import sqrt
print("Podaj dane równania kwadratowego Ax2+Bx+C=0:")
a = float(input("Podaj A:"))
b = float(input("Podaj B:"))
c = float(input("Podaj C:"))

delta = b**2-(4*a*c)
pierwdelta = 0
if delta>0:
    pierwdelta = sqrt(delta)
elif delta<0:
    print("Brak rozwiązań, delta<0")

def pierwiastki(delta, pierwdelta,a,b,c):
    if a!=0:
        if delta == 0:
            return f"Pierwiastek tego równania to: {-b/2*a}"
        elif delta>0:
            x1 = (-b-pierwdelta)/(2*a)
            x2 = (-b+pierwdelta)/(2*a)
            return f"Pierwiastki to x1: {x1}, x2: {x2}"

if a!=0:
    print(pierwiastki(delta, pierwdelta,a,b,c))
elif a==0:
    if b==0:
        if c==0:
            print("Nieskończenie wiele rozwiązań")
        else:
            print("Brak rozwiązań")


