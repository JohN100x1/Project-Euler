def sum_digit(n: int) -> int:
    """Get the digit sum of a positive integer n."""
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum
