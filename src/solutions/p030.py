from config import DIGIT_FIFTH_POWER


def sum_digits_fifth_power(n: int) -> int:
    """Get the sum of the fifth power of the digits of n."""
    return sum(DIGIT_FIFTH_POWER[d] for d in str(n))


def sum_all_digits_fifth_power() -> int:
    """
    Get the sum of all numbers that are equal to
    the sum of their digit fifth powers.

    max 6-digits because max value of 7-digit number
    is 7*9^5 which has 6 digits
    """
    return sum(n for n in range(2, 10**6) if sum_digits_fifth_power(n) == n)
