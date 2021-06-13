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

def quadratic_primes_longest_pair_product(N):
    qp_pairs = {}
    for a in range(-1000,1000):
        for b in PRIMES[PRIMES < 1000]:
            for n in range(1,N+1):
                if int(n**2 + a*n + b) not in PRIMES:
                    qp_pairs[(a,b)] = n-1
                    break
            else:
                qp_pairs[(a,b)] = n
    max_pair = max(qp_pairs, key=qp_pairs.get)
    product = max_pair[0] * max_pair[1]
    return product

print(quadratic_primes_longest_pair_product(100))