from math import factorial


def sum_digit_factorial(n: int) -> int:
    """Get the sum of the digits of n!."""
    digit_sum = sum(int(digit) for digit in str(factorial(n)))
    return digit_sum
