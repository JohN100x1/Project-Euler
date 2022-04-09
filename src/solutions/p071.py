from math import gcd


def get_max_numerator_three_sevenths() -> int:
    """
    Get the numerator of the fraction to the left of 3/7 when the proper
    fractions n/d are arranged in order for 1 < n < d <= 10^6.
    """
    max_n = 0
    max_nd = 0.0
    for d in range(10**6, 4, -1):
        for n in range((3 * d - 1) // 7, (3 * d) // 7):
            if 7 * n < 3 * d and gcd(n, d) == 1:
                if n / d > max_nd:
                    max_n = n
                    max_nd = n / d
    return max_n
