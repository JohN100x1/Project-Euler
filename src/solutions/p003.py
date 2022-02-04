from utils.primes import get_primes


def get_largest_prime_factor(n: int) -> int:
    """Get the largest prime factor of n."""
    sqrtn = int(n**0.5) + 1
    primes = get_primes(sqrtn)
    for p in reversed(primes):
        if n % p == 0:
            return p
    return n
