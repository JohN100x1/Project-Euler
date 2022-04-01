from utils.primes import miller_rabin_is_prime


def get_first_side_length_prime_sub_ratio(ratio: float) -> int:
    """
    Get the side length of Ulam spiral square such that the ratio of primes
    to the numbers on the diagonal is less than the given ratio.
    """
    count_primes = 0
    total = 1
    for x in range(1, 100000):
        four_x_sq = 4 * x**2 + 1
        corners = range(four_x_sq - 2 * x, four_x_sq + 4 * x + 1, 2 * x)
        count_primes += sum(
            1 for corner in corners if miller_rabin_is_prime(corner)
        )
        total += 4
        if count_primes / total < ratio:
            return 2 * x + 1
