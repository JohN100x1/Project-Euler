from utils.primes import get_primes


def count_prime_power_triples(m: int) -> int:
    """Get the number of n = p^2 + q^3 + r^4 < m for primes p, q, and r."""

    primes_squares = [p**2 for p in get_primes(int((m - 24) ** 0.5))]
    primes_cubes = [p**3 for p in get_primes(int((m - 20) ** (1 / 3)))]
    primes_quads = [p**4 for p in get_primes(int((m - 12) ** 0.25))]

    nums = set()

    for p in primes_squares:
        for q in primes_cubes:
            for r in primes_quads:
                total = p + q + r
                if total < m:
                    nums.add(total)
    return len(nums)
