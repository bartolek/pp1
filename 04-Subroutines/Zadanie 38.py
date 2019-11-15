text = input("Wpisz tekst: ")

def duzelitery(text):
    result = str()
    for i in text:
        if i.isupper():
            result+=i
    return result
print(duzelitery(text))