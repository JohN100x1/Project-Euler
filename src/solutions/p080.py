from decimal import Decimal, getcontext


def sum_digit_sqrt(n: int) -> int:
    """Get the sum of the first 100 decimal digits of sqrt n."""
    getcontext().prec = 105
    return sum(Decimal(n).sqrt().as_tuple()[1][:100])


def sum_digit_sqrt_sums(max_n: int) -> int:
    """
    Get the sum of the digit sums of sqrt n for 1 < n < max_n Where n is not
    a perfect square.
    """
    square_numbers = {n**2 for n in range(1, int(max_n**0.5) + 1)}
    digit_sums = 0
    for n in range(1, max_n + 1):
        if n in square_numbers:
            continue
        digit_sums += sum_digit_sqrt(n)
    return digit_sums
