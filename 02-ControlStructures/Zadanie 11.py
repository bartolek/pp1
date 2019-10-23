login = "marek"
hasło = "m-123"
    
login1 = input("Podaj login: ")

if login1 == login:
    
    hasło1 = input("Podaj hasło: ")
    if hasło1 == hasło:
        print("Login i hasło są zgodne.  Zostałeś zalogowany.")
    else:
        print("Wpisane hasło jest niepoprawne")

elif login1 != login:
    print("Podany login nie istnieje w systemie")
    