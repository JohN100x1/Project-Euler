from math import log

from utils.primes import get_primes


def get_nth_prime(n: int) -> int:
    """Get the n-th prime."""
    ubound = int(n * (log(n) + log(log(n))))
    nth_prime = get_primes(ubound)[n - 1]
    return nth_prime
