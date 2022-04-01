def count_sqrt2_continued_fraction_numer_digit(n: int) -> int:
    """
    Get the number of fractions in the first n expansions of sqrt 2 such that
    the numerator has more digits than the denominator.
    """
    count = 0
    numerator = 1
    denominator = 2
    for i in range(n + 1):
        numerator, denominator = denominator, 2 * denominator + numerator
        if len(str(numerator + denominator)) > len(str(denominator)):
            count += 1
    return count
