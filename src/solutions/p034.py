from config import DIGIT_FACTORIALS


def sum_equal_digit_factorial(max_n: int) -> int:
    """
    Get the sum of all numbers equal to the sum of their digit factorials.
    """
    equal_digit_factorials = set()
    for n in range(3, max_n + 1):
        if sum(DIGIT_FACTORIALS[d] for d in str(n)) == n:
            equal_digit_factorials.add(n)
    return sum(equal_digit_factorials)
