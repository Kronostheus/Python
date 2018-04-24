import math

def primeFactors(n):
    biggest = 0
    while n % 2 == 0:
        n = n / 2
    # Every composite number has at least one prime factor less than or equal to square root of itself
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            n = n / i
            if i > biggest:
                biggest = i
    return biggest

print(primeFactors(600851475143))