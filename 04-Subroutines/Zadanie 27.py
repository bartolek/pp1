import re

text = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."

def vowel(text):
    x = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(x)):
        print(f"{len(re.findall(x[i],text))} times {x[i]}")

        
vowel(text)

