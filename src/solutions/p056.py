def get_max_digit_sum(n: int) -> int:
    """Get the maximum digit sum of a^b where a, b < n."""
    max_digit_sum = 0
    for a in range(1, n):
        for b in range(1, n):
            digit_sum = sum(int(d) for d in str(pow(a, b)))
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    return max_digit_sum
