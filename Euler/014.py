# cache numbers we already calculated, along with their iteration
cache = {}

def collatz(num):
    count = 1
    temp = num
    while temp > 1:
        if temp % 2 == 0:
            temp = int(temp/2)
            # checks if we did this number already
            if temp in cache:
                count += cache[temp]
                break
            else:
                count += 1
        else:
            temp = 3 * temp + 1
            # checks if we did this number already
            if temp in cache:
                count += cache[temp]
                break
            else:
                count += 1
    # update cache
    cache[num] = count
    # return iteration
    return count

def res():
    num=0
    greatest=0
    for i in range(1, 1000000):
        curr = collatz(i)
        if num < curr:
            num = curr
            greatest = i
    print(greatest, " ",num)

res()