import math

# was sleepy, thought we just wanted all the primes until N
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

# realized I wasn't doing the correct thing   
def nthPrime(n):
    if n == 2:
        return 2
    # found out there is a pretty good prime aproximation
    # https://en.wikipedia.org/wiki/Prime_number_theorem#Statement
    # By doubling the aproximation we will have excess iterations but reduce the error (I was stubborn and didn't want to rewrite code)
    num = int(2 * n * math.log(n))
    return primes(num)[n-1]

print(nthPrime(10001))

