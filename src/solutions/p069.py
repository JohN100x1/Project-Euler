from utils.primes import get_primes


def get_phis(n: int) -> list[int]:
    """Get a list of values from Euler's phi function using primes."""
    phis = [i for i in range(2, n + 1)]
    for p in get_primes(n):
        phis[p - 2 :: p] = [k - k // p for k in phis[p - 2 :: p]]
    return phis


def get_max_ratio(max_n: int) -> int:
    """Get the value of n such that n/phi(n) is maximum."""
    max_idx = 0
    max_ratio = 0.0
    phis = get_phis(max_n)
    for n, phi in enumerate(phis, 2):
        r = n / phi
        if r > max_ratio:
            max_idx = n
            max_ratio = r
    return max_idx
