# http://mathworld.wolfram.com/DecimalExpansion.html
# http://mathworld.wolfram.com/RepeatingDecimal.html

def cycle(d):
    for t in range(1, d):
        # http://mathworld.wolfram.com/DecimalExpansion.html (7)
        # t = period
        # d = denominator
        if 1 == 10 ** t % d:
            return t
    # assumes 1 as default -> 1/2 = 0.5000000...
    return 1

def compute():
    longest = (1,1)
    for denominator in range(1000):
        temp = cycle(denominator)
        if longest[0] < temp:
            longest = denominator, temp
    # returns denominator and period
    return longest

print(compute())