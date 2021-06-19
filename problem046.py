import numpy as np

def get_primes(n):
    numbers = np.arange(n+1, dtype=np.int64)
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2,(n+1)//i+1):
                if j*i <= n:
                    is_prime[j*i] = False
        else:
            continue
    return numbers[is_prime]

PRIMES = get_primes(10000)

def twice_sq(N):
    return [2*n**2 for n in range(1, N+1)]

def odd_nums():
    n = len(PRIMES[PRIMES > 2])
    ptsqsums = set()
    t_sq = twice_sq(n)
    # Get prime + twice square set
    for i, p in enumerate(PRIMES[PRIMES > 2]):
        for j, tsq in enumerate(t_sq):
            ptsqsums.add(p + tsq)
    smallest_composite = None
    # Check if odd composite is in set
    for odd in range(9, PRIMES[-1], 2):
        if odd not in PRIMES and odd not in ptsqsums:
            smallest_composite = odd
            break
    return smallest_composite

print(odd_nums())