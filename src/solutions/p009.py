def get_pytriple_prod(n: int) -> int:
    """Get abc such that a^2+b^2=c^2 and a+b+c=n"""
    for a in range(1, n // 2 + 1):
        numer = n**2 // 2 - n * a
        denom = n - a
        if numer % denom == 0:
            b = numer // denom
            abc = a * b * (n - a - b)
            return abc
