from collections import defaultdict


def get_sqrt_period(n: int) -> int:
    """Get the Period the of the continued fraction of the sqrt n."""
    idx = 0
    qr: dict[tuple[int, int, int], int] = defaultdict(int)

    sqrtn = n**0.5
    a = int(sqrtn)
    t = sqrtn - a
    q = -a
    r = 1

    period = None
    while period is None:
        a = int(1 / t)
        q, r = -q - (a * (n - q**2) // r), (n - q**2) // r
        if (a, q, r) in qr:
            period = idx - qr[(a, q, r)]
        qr[(a, q, r)] = idx
        idx += 1
        t = (sqrtn + q) / r
    return period


def count_odd_sqrt_periods(max_n: int) -> int:
    """
    Get the number of odd periods for the continued fraction for sqrt n.
    Count up to and including sqrt max_n. Ignore perfect squares.

    https://www.desmos.com/calculator/z0by6836zy
    """
    count = 0
    for n in range(max_n + 1):
        if int(n**0.5) != n**0.5:
            period = get_sqrt_period(n)
            if period % 2 == 1:
                count += 1
    return count
