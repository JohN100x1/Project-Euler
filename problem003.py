def get_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def get_largest_prime_factor(n: int) -> int:
    sqrtn = int(n**0.5) + 1
    primes = get_primes(sqrtn)
    for p in reversed(primes):
        if n % p == 0:
            return p
    return n

print(get_largest_prime_factor(600851475143))