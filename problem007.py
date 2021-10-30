import numpy as np

def get_nth_prime(n):
    ubound = int(n*(np.log(n)+np.log(np.log(n))))
    sieve = [True] * ubound
    for i in range(3,int(ubound**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((ubound-i*i-1)//(2*i)+1)
    primes = [2] + [i for i in range(3,ubound,2) if sieve[i]]
    return primes[n-1]

print(get_nth_prime(10001))