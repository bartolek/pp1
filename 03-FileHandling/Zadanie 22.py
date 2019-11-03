with open("students.txt", "r")as file:
    for line in file:
        x = line.split(",")
        if x[2].isdigit() and int(x[2])<30:
            imie = x[0]
            nazwisko = x[1]
            email = x[4]
            print(imie,nazwisko,email)
