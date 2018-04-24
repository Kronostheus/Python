# want to avoid recursive functions on this one
def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

def getSum(fact):
    total = 0
    # iterate through the number as a string so we can easily access each digit
    for digit in str(fact):
        # return digit to int form and add it
        total += int(digit)
    return total

print(getSum(factorial(100)))