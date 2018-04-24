import itertools
# while looking around, I found out python library itertools already had a permutation function 
def solve():
    # we use string to avoid having to iterate through an int list and outputing to a string
    permutations = list(itertools.permutations("0123456789"))

    # this will group up all the numbers
    print(''.join(permutations[999999]))
solve()