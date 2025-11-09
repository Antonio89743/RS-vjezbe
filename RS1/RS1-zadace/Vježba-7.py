def run():

    password = input("Unesite lozinku: ").strip()
    provjera_lozinke(password)


def provjera_lozinke(password):
    if len(password) < 8 or len(password) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return
    
    has_number = False
    has_upper = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_number = True
        
    if has_upper == False:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    if has_number == False:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return

    if "password" in password.lower() or "lozinka" in password.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")

    print("Lozinka je jaka!")

run()