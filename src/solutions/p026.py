def get_cycle_len(d: int, max_iterations=1000) -> int:
    """Get the decimal digit cycle length of 1/d."""
    # Dict {(div, remainder) : idx)} to keep track of cycle repeat.
    div_remainder = {}
    # Long division of 1/d
    div = d
    remainder = 1
    quotient = 1
    index = 0
    while (div, remainder) not in div_remainder:
        div_remainder[(div, remainder)] = index
        div = quotient // d
        remainder = quotient % d
        quotient = 10 * remainder
        index += 1
    return index - div_remainder[(div, remainder)]


def get_max_cycle(n: int) -> int:
    """Get 1 < d < n such that 1/d has the longest decimal digit cycle."""
    max_d = 1
    max_cycle_len = 0
    for d in range(2, n):
        cycle_len = get_cycle_len(d)
        if cycle_len > max_cycle_len:
            max_d = d
            max_cycle_len = cycle_len
    return max_d
