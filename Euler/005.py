import math

# lowest common multiple
def lcm(a, b):
    # math.gcd -> greatest commom diviser
    return a * b // math.gcd(a, b)

def lcm_untilNum(num):
    total = 1
    for i in range(2, num + 1):
        total = lcm(i, total)
    return total

print(lcm_untilNum(20))