import math

# using modified 007.py answer
def primes(num):
    prime_sum = 0
    sieve_list = [True] * (num+1)
    sz = int(math.sqrt(num))

    # use a Sieve of Eratosthenes to compute primes
    for i in range(2, sz+1):
        if sieve_list[i]:
            for j in range(i*i, num, i):
                sieve_list[j] = False
    
    for i in range(2, num):
        if sieve_list[i]:
            prime_sum += i
    return prime_sum

print(primes(2000000))