import re

zdanie = "To be, or not to be, that is the question"
samogłoski = re.findall('(a|e|i|o|u|y|A|E|I|O|U|Y)',zdanie)
print("W tym zdaniu znajduje się", len(samogłoski), "samogłosek")