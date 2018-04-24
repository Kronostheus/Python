def fib():
    total = 2
    a = 1
    b = 2
    while True:
        c = a + b
        a = b
        b = c
        if b > 4000000:
            break
        elif b % 2 == 0:
            total += b
    return total

print(fib())