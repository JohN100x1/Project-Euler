def get_next_tph(n: int = 143) -> int:
    """
    Get the next T(a) = P(b) = H(c) such that c > n
    """
    a = n + 1
    while (1 + 24 * a * (2 * a - 1)) ** 0.5 % 6 != 5:
        a += 1
    c = 2 * a - 1
    tri = c * (c + 1) // 2
    return tri
