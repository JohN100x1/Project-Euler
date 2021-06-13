import numpy as np

def prime_sieve_nth(n):
    # m is the upper bound for the n-th prime
    m = int(n*(np.log(n)+np.log(np.log(n))))
    numbers = np.arange(m+1)
    numidx = np.ones(m+1, dtype=bool)
    numidx[0] = False
    numidx[1] = False
    for i in range(2, m+1):
        if numidx[i]:
            for j in range(2,(m+1)//i):
                numidx[j*i] = False
        else:
            continue
    return numbers[numidx][n-1]

print(prime_sieve_nth(10001))