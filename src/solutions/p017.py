SUB20_LETTERS = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
}
OVR20_LETTERS = {0: 0, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}


def count_letters(n: int) -> int:
    """Get number of letters for word of number n."""
    hundreds = SUB20_LETTERS[n // 100] + 7
    if n < 100:
        hundreds = 0
    elif n % 100 == 0:
        if n == 1000:
            return SUB20_LETTERS[n // 1000] + 8
        return hundreds
    else:
        hundreds += 3
    if n % 100 < 20:
        return SUB20_LETTERS[n % 100] + hundreds
    return SUB20_LETTERS[n % 10] + OVR20_LETTERS[(n % 100) // 10] + hundreds


def sum_letters(max_n: int) -> int:
    """
    Get the total number of letters for all words of numbers n where
    1 <= n <= max_n <= 1000.
    """
    return sum(count_letters(n) for n in range(1, max_n + 1))
