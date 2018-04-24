import math

# 021.py
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

# get all abudant numbers for 1 to 28124
def getAbdundantsList():
    abundants = []
    for i in range(1, 28124):
        if calc(i) > i:
            abundants.append(i)
    return abundants

# returns list where every number has been tested if they can be the sum of two abundant numbers
def isAbdSum():

    # abundant list
    abundants = getAbdundantsList()

    # list to be returned; every number starts at False
    lst = [False]*28124

    for i in range(len(abundants)):
        # previous numbers have already been tested
        for j in range(i, len(abundants)):
            # list is ordered, therefore we can exit inner loop if we exceed 28123 (besides lst not having enough space for it, every number would be true)
            if abundants[i] + abundants[j] > 28123:
                break
            lst[abundants[i] + abundants[j]] = True
    return lst

def solution():
    sum = 0
    abdSumList = isAbdSum()
    for i in range(28123):
        # if i is not in the list off all abundant sums, add it
        if not abdSumList[i]:
            sum += i
    return sum

print(solution())