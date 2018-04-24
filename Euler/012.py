import math

def divisors(num):
    total = 0
    sz = int(math.sqrt(num)) + 1
    for i in range(1, sz):
        if num % i == 0:
            # we must be mindful of perfect squares (ex: 144 has 15 divisors, if we just added 2 the result would be 16)
            total += 1 if i * i == num else 2
    return total

def triangle_divisors():
    cur = 1
    n = 1
    while True:
        n += 1
        cur += n
        if divisors(cur) >= 500:
            print(cur)
            break

triangle_divisors()