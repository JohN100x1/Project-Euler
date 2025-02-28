def sum_even_fib(n: int) -> int:
    """Sum of even fibonacci numbers less than or equal to n"""
    sum_even = 0
    fa, fb = 1, 1
    while fb < n:
        if fb % 2 == 0:
            sum_even += fb
        fa, fb = fb, fa + fb
    return sum_even
