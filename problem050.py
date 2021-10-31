import numpy as np

def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(1000000)

def get_longest_prime_sum():
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

print(get_longest_prime_sum())