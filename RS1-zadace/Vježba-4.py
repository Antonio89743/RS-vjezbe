def run():
    array_of_numbers = []

    while True:
        number_str = input("Unesite broj (ili 'kraj' za završetak unosa): ").strip()
        if number_str == '0':
            print("Uneseni brojevi su:")
            for num in array_of_numbers:
                print(num)
            break
        try:
            number = int(number_str)
            array_of_numbers.append(number)
        except ValueError:
            print("Greška: Unesite validan broj!")


run()