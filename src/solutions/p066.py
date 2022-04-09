def get_sqrt_seq(n: int, len_seq: int) -> list[int]:
    """Get a list of len_seq terms for the continued fraction of sqrt n."""
    idx = 0
    sqrtn = n**0.5
    seq = [int(sqrtn)]
    a = int(sqrtn)
    t = sqrtn - a
    q = -a
    r = 1

    for i in range(len_seq - 1):
        a = int(1 / t)
        q, r = -q - (a * (n - q**2) // r), (n - q**2) // r
        seq.append(a)
        idx += 1
        t = (sqrtn + q) / r
    return seq


def get_sqrt_convergent(n: int, len_seq: int) -> tuple[int, int]:
    """
    Get the numerator and denominator of the len_seq-th continued fraction of
    the sqrt n.
    """
    sqrt_seq = get_sqrt_seq(n, len_seq)
    den = 1
    numer = sqrt_seq[len_seq - 1]
    for k in range(2, len_seq + 1):
        numer, den = numer * sqrt_seq[len_seq - k] + den, numer
    return numer, den


def get_max_diophantine(max_d: int) -> int:
    """
    Get D <= max_D such that x^2 - D*y^2 = 1 has a solution where x is maximum.
    """
    sol_d = 0
    max_x = 0
    for D in range(2, max_d + 1):
        if D**0.5 == int(D**0.5):
            continue
        i = 0
        x, y = get_sqrt_convergent(D, i)
        while x**2 - D * y**2 != 1:
            i += 1
            x, y = get_sqrt_convergent(D, i)
        if x > max_x:
            max_x = x
            sol_d = D
    return sol_d
