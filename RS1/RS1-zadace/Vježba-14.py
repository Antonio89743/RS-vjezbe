#  Zadatak 1

def isPrime(integer):
    if integer <= 1:
        return False
    for i in range(2, int(integer**0.5) + 1):
        if integer % i == 0:
            return False
    return True

print("is Prime")
print(isPrime(7))
print(isPrime(10))



# Zadatak 2

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if isPrime(num):
            primes.append(num)
    return primes

print("\nPrimes in range")
print(primes_in_range(1, 10))