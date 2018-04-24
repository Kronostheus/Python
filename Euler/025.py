# we alter very slightly 002.py solution
def fib():
    total = 2
    a = 1
    # alter B since we now start 1 1 and not 1 2 like 002.py
    b = 1
    # we convert the current number into a string so we can count its digits (with the length of the string)
    while len(str(b)) < 1000:
        c = a + b
        a = b
        b = c
        total += 1
    return total

print(fib())