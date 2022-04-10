def sum_term(a_plus_b: int, c: int, n: int) -> int:
    """Get the value of the term."""
    return max((a_plus_b * n) // 2 + 1 - max(a_plus_b * n - c * n, 1), 0)


def count_cuboid_sol(m: int) -> int:
    """
    Get the number of distinct cuboid solutions.
    Solve for integers d**2 = (a + b)**2 + c**2 where a <= b <= c.
    """
    sol_count = 0
    ubound = (m + m * (5**0.5 / 2)) ** 0.5
    family = set()
    two_m = 2 * m
    for x in range(2, int(ubound) + 1):
        for y in range(1, x):
            a_plus_b = x**2 - y**2
            c = 2 * x * y
            d = x**2 + y**2

            normed = (a_plus_b / d, c / d)
            if a_plus_b <= two_m and c <= m and normed not in family:
                n_values = range(1, min(two_m // a_plus_b, m // c) + 1)
                sol_count += sum(sum_term(a_plus_b, c, n) for n in n_values)
                family.add((a_plus_b / d, c / d))

            a_plus_b, c = c, a_plus_b
            normed = (a_plus_b / d, c / d)
            if a_plus_b <= two_m and c <= m and normed not in family:
                n_values = range(1, min(two_m // a_plus_b, m // c) + 1)
                sol_count += sum(sum_term(a_plus_b, c, n) for n in n_values)
                family.add((a_plus_b / d, c / d))
    return sol_count


def get_cuboid_size_solutions_over(k: int) -> int:
    """
    Get the lowest M such that there are over k distinct cuboids with
    dimensions up to M x M x M with the 'shortest' path being an integer.
    """
    lbound, ubound = 1, 2
    lower_count = count_cuboid_sol(lbound)
    upper_count = count_cuboid_sol(ubound)
    # Range-search for M
    while k < lower_count or k > upper_count:
        lbound *= 2
        ubound *= 2
        lower_count = count_cuboid_sol(lbound)
        upper_count = count_cuboid_sol(ubound)
    # Binary search for M
    while lbound + 1 != ubound:
        mid = (lbound + ubound) // 2
        mid_count = count_cuboid_sol(mid)
        if mid_count < k:
            lbound = mid
        elif mid_count > k:
            ubound = mid
    return ubound
