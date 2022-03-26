def sum_diagonals_ulam_spiral(n: int) -> int:
    """
    Get the sum of the numbers on a nxn Ulam spiral.
    https://www.desmos.com/calculator/eqr1s8kxcn
    """
    diagonal_sum = (n + 1) * (4 * n**2 - n + 9) // 6 - 3
    return diagonal_sum
