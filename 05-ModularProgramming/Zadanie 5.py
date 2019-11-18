import statistics
Płaca = [21600,4350,3920,5590,3250,4010]

def SredniaArytmetyczna(Płaca):
    return statistics.mean(Płaca)
def Mediana(Płaca):
    return statistics.median(Płaca)
def OdchylenieStandardowe(Płaca):
    return statistics.stdev(Płaca)
    


print(f"Średnia płaca: {SredniaArytmetyczna(Płaca)}")
print(f"Mediana: {Mediana(Płaca)}")
print(f"Odchylenie Standardowe: {OdchylenieStandardowe(Płaca)}")