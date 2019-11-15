imie = "Wojtek"
imiona = ["Janek", "Ania", "Wojtek", "Zosia"]

def jestimie(imie,imiona):
    x = "Imie nie jest zawarte w wykazie imion"
    for i in range(len(imiona)):
        if imiona[i]==imie:
            x = "Imię zawarte jest w wykazie imion"
            break
    return x

jestimie(imie,imiona)

print(jestimie(imie,imiona))