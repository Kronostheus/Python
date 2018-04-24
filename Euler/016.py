def sumPower(num, pow):
    sz = num ** pow
    result = 0
    for i in str(sz):
        result += int(i)
    print(result)

sumPower(2,1000)