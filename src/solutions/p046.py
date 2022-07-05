from utils.exceptions import SolutionNotFoundError
from utils.primes import get_primes


def get_goldbach_counter_example(n: int = 10000) -> int:
    """
    Gets the smallest prime that can't be written as the sum of a prime
    and twice a square where any prime less than n is considered.
    """

    primes = get_primes(n)
    prime_set = set(primes)
    odd_primes = primes[1:]

    tsq_sums = set()
    # Get prime + twice square set
    for p in odd_primes:
        q = 1
        tsq = p + 2 * q**2
        while tsq < primes[-1]:
            tsq_sums.add(tsq)
            q += 1
            tsq = p + 2 * q**2
    # Check if odd composite is in set
    for odd in range(9, primes[-1], 2):
        if odd not in prime_set and odd not in tsq_sums:
            return odd
    raise SolutionNotFoundError("Goldbach counter example not found.")
