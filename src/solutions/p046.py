def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10000)
PRIME_SET = set(PRIMES)
ODD_PRIMES = PRIMES[1:]

def get_goldbach_counter_example():
    ptsqsums = set()
    # Get prime + twice square set
    for p in ODD_PRIMES:
        q = 1
        tsq = p + 2*q**2
        while tsq < PRIMES[-1]:
            ptsqsums.add(tsq)
            q += 1
            tsq = p + 2*q**2
    # Check if odd composite is in set
    for odd in range(9, PRIMES[-1], 2):
        if odd not in PRIME_SET and odd not in ptsqsums:
            return odd

print(get_goldbach_counter_example())