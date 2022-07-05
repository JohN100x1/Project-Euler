from utils.exceptions import SolutionNotFoundError
from utils.primes import get_primes, miller_rabin_is_prime


class PrimeContext:
    """Check primes using a prime set."""

    PRIME_SET = set(get_primes(1000000))

    @classmethod
    def fast_is_prime(cls, n: int) -> bool:
        """Return boolean of whether n is a prime."""
        if n < 1000000:
            return n in cls.PRIME_SET
        else:
            return miller_rabin_is_prime(n)


def is_pair(p: int, q: int) -> bool:
    """Return boolean of whether p and q concatenate to form a prime."""
    p_string, q_string = str(p), str(q)
    num1, num2 = int(p_string + q_string), int(q_string + p_string)
    if PrimeContext.fast_is_prime(num1) and PrimeContext.fast_is_prime(num2):
        return True
    return False


def sum_min_five_prime_pairs() -> int:
    """Get the lowest sum of 5 primes which pairwise concatenate to a prime."""
    primes = get_primes(10**4)
    # prime mod 3 = 1 must concatenate to prime mod 3 = 1
    # prime mod 3 = 2 must concatenate to prime mod 3 = 2
    # two_primes have been skipped when it should not
    one_primes = [3] + [p for p in primes if p % 3 == 1]
    len_one_primes = len(one_primes)

    for i, p in enumerate(one_primes):
        for j in range(i + 1, len_one_primes):
            q = one_primes[j]
            if not is_pair(p, q):
                continue
            for k in range(j + 1, len_one_primes):
                r = one_primes[k]
                if not is_pair(p, r) or not is_pair(q, r):
                    continue
                for a in range(k + 1, len_one_primes):
                    s = one_primes[a]
                    if any(not is_pair(x, s) for x in (p, q, r)):
                        continue
                    for b in range(a + 1, len_one_primes):
                        t = one_primes[b]
                        if all(is_pair(x, t) for x in (p, q, r, s)):
                            return sum((p, q, r, s, t))
    raise SolutionNotFoundError("Failed to solve p060.")
