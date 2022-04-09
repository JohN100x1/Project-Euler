from utils.primes import get_primes


def sum_phis(n: int) -> int:
    """Get the sum of phi(m) for m <= n."""
    primes = get_primes(n)
    phis = [i for i in range(2, n + 1)]
    for p in primes:
        phis[p - 2 :: p] = [k - k // p for k in phis[p - 2 :: p]]
    return sum(phis)
