def sum_3_5_multiples(n: int) -> int:
    """Sum of multiples of 3 and 5 less than n."""
    n3 = (n - 1) // 3
    n5 = (n - 1) // 5
    n15 = (n - 1) // 15
    s = (3 * n3 * (n3 + 1) + 5 * n5 * (n5 + 1) - 15 * n15 * (n15 + 1)) // 2
    return s
