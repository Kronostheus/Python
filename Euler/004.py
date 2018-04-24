def palindrome():
    biggest = 0
    # counting backwards for greater numbers
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            cand = i *j
            # convert to string and compare with it's reverse
            if str(cand) == str(cand)[::-1] and cand > biggest:
                biggest = cand
    return biggest

print(palindrome())