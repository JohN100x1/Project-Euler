def get_min_pentagonal_diff(n: int = 3000) -> int:
    """
    Gets the minimum difference between two pentagonal numbers Pi > Pj > 0
    such that Pi - Pj and Pi + Pj are pentagonal where i <= n.

    https://www.desmos.com/calculator/q44wzac3qg
    # TODO : proper solution requires checking Pi - Pj is minimal
    """
    pentagonals = [n * (3 * n - 1) // 2 for n in range(1, int(1.5 * n))]
    set_pentagonals = set(pentagonals)
    diff = 1e400
    for i, pi in enumerate(pentagonals, 1):
        for j in range(int((1 + (72 * i - 47) ** 0.5) / 6), i):
            pj = pentagonals[j - 1]
            p_sum = pi + pj
            p_sub = pi - pj
            if p_sum in set_pentagonals and p_sub in set_pentagonals:
                if p_sub < diff:
                    diff = p_sub
    return diff
