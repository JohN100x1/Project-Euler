import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def count_ncr_greater_than(N):
    count = 0
    for n in range(1, 101):
        for r in range(n + 1):
            if ncr(n, r) > N:
                count += 1
    return count

print(count_ncr_greater_than(10**6))