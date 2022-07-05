from config import NON_ZERO_DIGITS


def is_pandigital_one_to_nine(dlist: list[int]) -> bool:
    """Check whether dlist is pandigital 1 to 9."""
    # Check set contains all digits
    if set(dlist) != NON_ZERO_DIGITS:
        return False
    # Check no repeats
    if len(dlist) != len(NON_ZERO_DIGITS):
        return False
    return True


def get_max_pandigital_concat() -> int:
    """
    Get the maximum 1-9 pandigital number formed from concatenating
    x * 1, x * 2, ...., x * n where n > 1 and x is some integer.

    Starting number must have less than 4 digits
    otherwise x * 1, x * 2, x * 3 has at least 12 digits
    """
    max_pandigital = 0
    ubound = pow(10, 4)
    for x in range(1, ubound):
        n = 1
        digits: list[int] = []
        while len(digits) < 9:
            product = x * n
            digits += list(map(int, str(product)))
            n += 1
        if len(digits) > 9:
            continue
        if is_pandigital_one_to_nine(digits):
            pandigital = int("".join(str(d) for d in digits))
            if pandigital > max_pandigital:
                max_pandigital = pandigital
    return max_pandigital
