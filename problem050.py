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

PRIMES = get_primes(1000000)

def find_longest_prime_sum():
    Psums = np.cumsum(PRIMES)
    Psums0 = np.zeros(len(Psums)+1, dtype="int32")
    Psums0[1:] = Psums
    p_found = False
    p = None
    # The sum of the First 547 primes >1 million
    for L in range(546, 0, -1):
        j = 0
        Psum = Psums[L+j] - Psums0[j]
        while Psum < 1000000:
            if Psum in PRIMES:
                p = Psum
                p_found = True
                break
            j += 1
            Psum = Psums[L+j] - Psums0[j]
        if p_found:
            break
    return p

print(find_longest_prime_sum())