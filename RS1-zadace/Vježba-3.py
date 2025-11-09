import random

def run():

    random_number = random.randint(1, 100)

    broj_je_pogoden = False
    number_of_attempts = 0
    while broj_je_pogoden == False:
        number_of_attempts += 1
        guess_str = input("Pogodi broj između 1 i 100: ").strip()

        try:
            guess = int(guess_str)
        except ValueError:
            print("Greška: Unesite validan broj!")
            continue

        if guess < random_number:
            print("Uneseni broj je premali! Pokušajte ponovo.")
        elif guess > random_number:
            print("Uneseni broj je prevelik! Pokušajte ponovo.")
        else:
            print(f"Bravo, pogodio si u {number_of_attempts} pokušaja")
            broj_je_pogoden = True
        


    
run()
