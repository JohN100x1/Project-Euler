def get_pytriple_prod(n):
    assert(n % 2 == 0)
    for a in range(1,n//2+1):
        numer = (n**2//2 - n*a)
        denom = (n - a)
        if numer % denom == 0:
            b = numer // denom
            abc = a*b*(n - a - b)
            return abc

print(get_pytriple_prod(1000))