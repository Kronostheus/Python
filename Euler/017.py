# 1-19
ONES = (0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8)
# 10-90
TENS = (0,3,6,6,5,5,5,7,6,6)

def countLetters(): 
    total = 0
    for i in range(1,1000):
        ones = i % 10 
        tens = ((i % 100) - ones) // 10 
        hundreds = ((i % 1000) - (tens * 10) - ones) // 100 
    
        if hundreds != 0:
            # hundred = 7
            total += ONES[hundreds] + 7
            if tens != 0 or ones != 0:
                total += 3 # and
        if tens == 0 or tens == 1:
            total += ONES[tens * 10 + ones]
        else:
            total += TENS[tens] + ONES[ones]
    # thousand = 8
    total += ONES[1] + 8
    print(total)

countLetters()