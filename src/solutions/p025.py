def get_nth_fibonacci_digits(d: int) -> int:
    """
    Get integer n such that the n-th fibonacci number has d > 0 or more digits.
    """
    if d == 1:
        return 1
    fa, fb = 1, 1
    n = 2
    while len(str(fa)) < d:
        fa, fb = fa + fb, fa
        n += 1
    return n
