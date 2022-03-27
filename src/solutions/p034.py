def sum_equal_digit_factorial(max_n: int) -> int:
    """
    Get the sum of all numbers equal to the sum of their digit factorials.
    """
    digit_factorial = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
    }
    equal_digit_factorials = set()
    for n in range(3, max_n + 1):
        if sum(digit_factorial[int(d)] for d in str(n)) == n:
            equal_digit_factorials.add(n)
    return sum(equal_digit_factorials)
