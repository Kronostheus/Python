def is_multiple(num):
    # return if either is true
    return num % 3 == 0 or num % 5 == 0

def sum():
    mulSum = 0
    for i in range(1000):
        if is_multiple(i):
            mulSum += i
    return mulSum

print(sum())