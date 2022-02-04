def sum_even_fib(n: int) -> int:
    """Sum of even fibonacci numbers less than or equal to n"""
    sum_even = 0
    fa, fb = 1, 1
    while fb < n:
        fa, fb = fb, fa + fb
        if fb % 2 == 0:
            sum_even += fb
    return sum_even
