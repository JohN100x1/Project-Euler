from utils.primes import get_primes


def get_min_phi_ratio_perm(max_n: int) -> int:
    """
    Get the values of 1 < n < 10^7 such that n and phi(n) are permutations and
    n/phi(n) is minimum.

    This is achieved when n = p1 * p2 for primes p1 and p2.
    Also, phi(p1 * p2) = (p1 - 1)(p2 - 1)
    """
    # Obviously you won't know the search range 10^3 < p < 10^4 beforehand
    bounded_primes = [p for p in get_primes(max_n) if 10**3 < p < 10**4]
    len_primes = len(bounded_primes)

    sol_n = 0
    min_ratio = float("inf")

    for i, p in enumerate(bounded_primes):
        for j in range(i + 1, len_primes):
            q = bounded_primes[j]
            n = p * q
            if n > 10000000:
                break
            phi = (p - 1) * (q - 1)
            ratio = n / phi
            if ratio < min_ratio and sorted(str(n)) == sorted(str(phi)):
                min_ratio = ratio
                sol_n = n
    return sol_n
