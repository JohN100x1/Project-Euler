def get_e_denominator(n: int) -> int:
    """Get the n-th denominator of the continued fraction of e."""
    if n == 1:
        return 2
    elif n % 3 == 0:
        return 2 * (n // 3)
    else:
        return 1


def get_e_convergent(n: int) -> tuple[int, int]:
    """
    Get the n-th numerator and denominator of the continued fraction of e.
    """
    den = 1
    numer = get_e_denominator(n)
    for k in range(1, n):
        numer, den = numer * get_e_denominator(n - k) + den, numer
    return numer, den


def sum_digits_e_convergent_numer(n: int) -> int:
    """
    Get the digit sum of the n-th numerator in the continued fraction of e.
    """
    numer, _ = get_e_convergent(n)
    return sum(map(int, str(numer)))
