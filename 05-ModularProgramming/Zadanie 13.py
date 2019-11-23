text = input("Wpisz tekst: ")

def wspak(text):
    return text[::-1]

def spacja(text):
    text2 = " "
    for i in text:
        text2+= i + " "
    return text2

def WielkaLitera(text):
    rozdzielony = text.split()
    Wielka = " "
    for word in rozdzielony:
        x=0
        for i in word:
            if x==0:
                a = i.upper()
            else:
                a = i.lower()
            Wielka+=a
            x+=1
        Wielka+= " "
    return Wielka
        
print(f"Wspak: {wspak(text)}")
print(f"Rozstrzelony ciąg: {spacja(text)}")
print(f"Wielka litera: {WielkaLitera(text)}")