text = input("Podaj ciąg znaków: ")
text2 = " "

for i in text:
    if i.isupper():
        text2+= i

print(text2)