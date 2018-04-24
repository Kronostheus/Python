import math

# very similiar to 012.py divisors() but this time we are interested in the sum of the divisors and not their quantity
def calc(num):
    sz = int(math.sqrt(num)) + 1
    divSum = 0
    for i in range(1, sz):
        if num % i == 0:
            # take care of perfect squares and the number itself (they have to be less than)
            if i * i == num or i == 1:
                divSum += i
            else:
                divSum += i + (num // i)
    return divSum

def compute(limit):
    total = 0
    for i in range(1, limit):
        # if d(a)=b and d(b)=a, where a != b, then a and b are an amicable pair
        if calc(calc(i)) == i and calc(i) != i:
            total += i
    return total


print(compute(10000))