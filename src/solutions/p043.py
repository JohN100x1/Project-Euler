def get_three_digit_multiples(k: int) -> list[str]:
    """
    Get all 3 digit multiples of k as a list of strings with
    leading zeros included.
    """
    multiples_strings = []
    multiples = [j for j in range(k, 1000, k) if j > 10]
    for m in multiples:
        mult = str(m)
        # Add zero if only 2-digits
        if len(mult) == 2:
            mult = "0" + mult
        # Check if digits are unique
        if len(mult) == len(set(mult)):
            multiples_strings.append(mult)
    return multiples_strings


def sum_zero_nine_pandigital_substring_div() -> int:
    """
    Get the sum of all 0-9 pandigital numbers with 3-substring divisibility.
    """
    digits = {str(j) for j in range(10)}
    divs = [13, 11, 7, 5, 3, 2]
    candidates = get_three_digit_multiples(17)
    for div in divs:
        follow_up = get_three_digit_multiples(div)
        possible_values = []
        for c in candidates:
            for f in follow_up:
                if f[1:] == c[:2]:
                    possible_values.append(f[0] + c)
        # Remove Repeating digit candidates
        candidates = [c for c in possible_values if len(c) == len(set(c))]
    # Remove leading zeros candidates
    candidates = [c for c in candidates if not c.startswith("0")]

    # Place remaining digit d1 since leading substring is any multiple.
    pandigital_sum = 0
    for c in candidates:
        remaining_digit = digits - set(c)
        pandigital_sum += int(remaining_digit.pop() + c)
    return pandigital_sum
