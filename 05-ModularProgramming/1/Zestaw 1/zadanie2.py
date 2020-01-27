def dodatek_stazowy(lata):
    dodatek = 0
    if lata <= 5:
        dodatek+= lata*100
    elif lata > 5 and lata <=8:
        dodatek+= 500 + (lata-5)*200
    elif lata > 8:
        dodatek+= 500 + 600 + (lata-8)*50
    return dodatek
