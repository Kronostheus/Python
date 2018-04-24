def triplets(perimeter):
    sz = round(perimeter / 2)
    for a in range(1, sz):
        for b in range(a+1, sz):
            c = perimeter - (a + b)
            if a * a + b * b == c * c:
                return (a*b*c, a, b, c)

print(triplets(1000))