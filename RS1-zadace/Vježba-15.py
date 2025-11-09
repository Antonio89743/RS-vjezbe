def count_vowels_consonants(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    return {
        'vowels': sum(1 for char in string if char in vowels),
        'consonants': sum(1 for char in string if char in consonants)
    }


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(tekst))
