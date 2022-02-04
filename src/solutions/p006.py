def sq_sum_diff(n: int) -> int:
    """
    Get the difference between the squared sum of 1 to n
    and the sum of squares from 1 to n.
    """
    sq_sum = n**2 * (n + 1) ** 2 // 4
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    diff = sq_sum - sum_sq
    return diff
