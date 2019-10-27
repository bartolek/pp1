x = int(input("Podaj wspolrzedna x: "))
y = int(input("Podaj wspolrzedna y: "))

if x > 0 and y > 0:
    print("Punkt P(%s,%s) znajduje się w pierwszej ćwiartce układu współrzędnych" % (x,y))
elif x > 0 and y < 0:
    print("Punkt P(%s,%s) znajduje się w czwartej ćwiartce układu współrzędnych" % (x,y))
elif  x < 0 and y > 0:
    print("Punkt P(%s,%s) znajduje się w drugiej ćwiartce układu współrzędnych" % (x,y))
elif x < 0 and y < 0:
    print("Punkt P(%s,%s) znajduje się w trzeciej ćwiartce układu współrzędnych" % (x,y))