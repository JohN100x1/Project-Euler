from utils.primes import get_primes


class PrimeContext:
    """Get the prime partitions using a prime set."""

    PRIMES = get_primes(10**2)
    PRIME_SET = set(PRIMES)

    @classmethod
    def count_prime_partition(cls, n0: int, n: int) -> int:
        """Get number of prime partitions of n starting with partition n0."""
        if n in {2, 3}:
            return 0
        count = 0
        for n1 in (p for p in cls.PRIMES if n0 <= p <= n // 2):
            n2 = n - n1
            if n2 in cls.PRIME_SET:
                count += 1 + cls.count_prime_partition(n1, n2)
            else:
                count += cls.count_prime_partition(n1, n2)
        return count


def get_prime_partition_count_over(m: int) -> int:
    """Get the first number which has over m ways to partition into primes."""
    n = 4
    while PrimeContext.count_prime_partition(2, n) < m:
        n += 1
    return n
