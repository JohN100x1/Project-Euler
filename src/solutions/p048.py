def sum_self_pow(n: int, d: int) -> int:
    """Get the sum of 1^1 + 2^2 + 3^3 + ... + n^n mod d."""
    self_pow_sum = 0
    for i in range(1, n + 1):
        self_pow_sum += pow(i, i, 10**d)
        self_pow_sum %= pow(10, d)
    return self_pow_sum
