def sqsumdiff(n: int) -> int:
    sqsum = n**2 * (n+1)**2/4
    sumsq = n*(n+1)*(2*n+1)/6
    diff = sqsum - sumsq
    return int(diff)

print(sqsumdiff(100))