from math import comb


def count_ncr_greater_than(m: int) -> int:
    """Count the number of n choose r greater than m for 1 <= n <= 100."""
    return sum(
        1 for n in range(1, 101) for r in range(n + 1) if comb(n, r) > m
    )
