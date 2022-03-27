from math import gcd


def get_denominator_digit_cancel_frac_product():
    """
    Gets the denominator of the product of all two digit cancelling fractions
    less than 1.

    e.g. 49/98 = 4/8 is a valid two digit cancelling fraction
    """
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    digit_cancelling_fractions = set()
    for a in digits:
        for b in digits - {a}:
            for c in digits - {a, b}:
                # Check only fractions < 1
                if b > c:
                    continue
                # Case 1: ab / ac = b / c
                # Case 2: ba / ca = b / c
                # Which is only true when b = c
                # This would mean b / c = 1, so it's skipped

                ab = 10 * a + b
                ca = 10 * c + a
                ba = 10 * b + a
                ac = 10 * a + c

                # Case 3: ab / ca = b / c
                if ab * c == b * ca:
                    digit_cancelling_fractions.add((ab, ca))
                # Case 4: ba / ac = b / c
                if ba * c == b * ac:
                    digit_cancelling_fractions.add((ba, ac))
    numerator, denominator = 1, 1
    for n, d in digit_cancelling_fractions:
        numerator *= n
        denominator *= d
    simple_denominator = denominator // gcd(numerator, denominator)
    return simple_denominator
