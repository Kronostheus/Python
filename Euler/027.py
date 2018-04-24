import math

# 007.py
def primes(num):
    prime_list = []
    sieve_list = [True] * (num+1)
    sz = int(math.sqrt(num))

    # use a Sieve of Eratosthenes to compute primes
    for i in range(2, sz+1):
        if sieve_list[i]:
            for j in range(i*i, num, i):
                sieve_list[j] = False
    
    # make list readable (numbers not booleans)
    for i in range(2, num):
        if sieve_list[i]:
            prime_list.append(i)
    return prime_list

# list of all primes under 1000
primeList = primes(1000)

# simple primality test: https://en.wikipedia.org/wiki/Primality_test#Pseudocode
def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def compute():
    longest = (0, 0, 0)

    # if n = 0 the equation will return 0**2+0*a+b = b, therefore, b must be prime
    for b in primeList:
        for a in range(-999, 1000):
            n = 0
            while isPrime((n**2) + (a*n) + b):
                n += 1
            if n > longest[0]:
                longest = n, a, b

    return longest[1] * longest[2]

print(compute())