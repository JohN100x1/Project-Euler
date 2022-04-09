def count_nth_digit_power() -> int:
    """
    Get the number of n-digit numbers which are n-th powers.

    https://www.desmos.com/calculator/ol6twhcock
    """
    count = 0
    n = 1
    lbound = pow(10, 1 - 1 / n)
    while lbound <= 9:
        count += 10 + int(-lbound // 1)
        n += 1
        lbound = pow(10, 1 - 1 / n)
    return count
