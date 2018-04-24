# exercise describes something like NE lattice paths which are counted by the binomial coefficient (and arranged in Pascal's Triangle)
def binomial(n, k):
    res = 1
    # symmetry of the binomal coefficient means we can set upper limit to the smaller of k and (n-k)
    for i in range(min(k, n-k)):
        # multiplicative formula is better suited to computation than recursive or factorial formulas
        res *= (n - i)
        res //= (i + 1)
    return res 

# the routes of a 20x20 grid will be from (0,0) to (20,20) therefore we want binomial(20+20, 20)=binomial(40,20)
print(binomial(40, 20))