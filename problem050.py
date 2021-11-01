import numpy as np

def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(1000000)
PRIME_SET = set(PRIMES)

def get_longest_prime_sum(N):
    Psums = np.cumsum(PRIMES)
    psums = np.zeros(len(Psums)+1, dtype="int32")
    psums[1:] = Psums
    # The sum of the First 547 primes >1 million
    for L in range(546, 0, -1):
        j = 0
        Psum = Psums[L+j] - psums[j]
        while Psum < N:
            if Psum in PRIME_SET:
                return Psum
            j += 1
            Psum = Psums[L+j] - psums[j]
    return None

print(get_longest_prime_sum(1000000))