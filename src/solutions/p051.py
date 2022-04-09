from collections import defaultdict

from utils.primes import get_primes


def get_smallest_eight_prime_value_family() -> int:
    """
    Get the smallest prime of an eight prime value family where digits of that
    prime are replaced with the same digit to form the other seven primes.

    For an 8 prime value family, 3 digits must be the same and last digit is
    unchanged.

    NOTE: since PRIMES < 10^6, there's only 1 repeated_digit
    """
    repeated = {}
    for p in get_primes(10**6):
        repeated_digit = None
        prime_string = str(p)[::-1]
        digit_lists = defaultdict(list)
        for i, d in enumerate(map(int, prime_string)):
            digit_lists[d].append(i)
            # Record indices of 3 digit repeats
            if len(digit_lists[d]) == 3:
                repeated_digit = d
        if repeated_digit is not None:
            repeated[p] = digit_lists.pop(repeated_digit)

    # Pick 3 digit positions from repeated digits
    for p, indexes in repeated.items():
        family = {p}
        sub = sum(p % pow(10, i + 1) - p % pow(10, i) for i in indexes)
        base = p - sub
        increment = sum(1 * pow(10, i) for i in indexes)
        for d in range(int(len(str(base)) < len(str(p))), 10):
            q = base + d * increment
            if q in repeated:
                family.add(q)
        if len(family) == 8:
            return min(family)
