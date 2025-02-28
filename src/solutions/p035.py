from utils.primes import get_primes


def get_circ_prime(p: int, prime_set: set[int]) -> set[int]:
    """
    Get a set of primes if p is a circular prime,
    Otherwise return an empty set.
    """
    m = len(str(p))
    cyc_nums = set()
    for j in range(m):
        div = pow(10, j)
        n = (p % div) * pow(10, m - j) + p // div
        if n not in prime_set:
            return set()
        cyc_nums.add(n)
    return cyc_nums


def count_circ_primes() -> int:
    """Get the number of circular primes in the list of PRIMES."""
    circ_primes = {2, 3, 5, 7}
    nope_digits = {0, 2, 4, 5, 6, 8}
    primes = get_primes(10**6)
    prime_set = set(primes)
    for p in primes:
        # Skip existing circular primes
        if p in circ_primes:
            continue

        # Circular primes with >2 digits don't have these digits
        if any(d in nope_digits for d in map(int, str(p))):
            continue

        # Roll the digits and check if they're prime
        cyc_nums = get_circ_prime(p, prime_set)
        circ_primes.update(cyc_nums)
    return len(circ_primes)
