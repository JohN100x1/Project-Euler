from math import prod


def get_digit_bin(n: int) -> tuple[int, int]:
    """Get the digit bin of the n-th champernowne digit."""
    m = 1
    while n > 9 * m * 10 ** (m - 1):
        n -= 9 * m * 10 ** (m - 1)
        m += 1
    return m, n


def champernowne_digit(n: int) -> int:
    """Get the n-th champernowne digit."""
    # Single digit case
    if n < 10:
        return n
    m, n = get_digit_bin(n)
    r = n % m
    if r == 0:
        return (n // m - 1) % 10
    elif r == 1:
        return (n // (m * 10 ** (m - r)) + 1) % 10
    else:
        return (n // (m * 10 ** (m - r))) % 10


def prod_nth_champernowne(nlist: list[int]) -> int:
    """Get the product of all n-th champernowne digits for n in nlist."""
    return prod(champernowne_digit(n) for n in nlist)
