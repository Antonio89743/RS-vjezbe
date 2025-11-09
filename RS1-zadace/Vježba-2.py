def run():
    godina_str = input("Unesite godinu: ").strip()

    try:
        godina = float(godina_str)


        if godina % 4 == 0:
            if godina % 100 == 0:
                if godina % 400 == 0:
                    print(f"Godina {int(godina)} je prijestupna.")
                else:
                    print(f"Godina {int(godina)} nije prijestupna.")
            else:
                print(f"Godina {int(godina)} je prijestupna.")

    except ValueError:
        print("Greška: Unesite validne brojeve!")
        return
    
run()
