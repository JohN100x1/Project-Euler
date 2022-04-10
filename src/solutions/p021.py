from utils.div import get_proper_factor_sums


def sum_amicable(n: int, limit=25000) -> int:
    """Get the sum of amicable numbers less than n."""
    checked = set()
    amicable_sum = 0
    proper_factor_sums = get_proper_factor_sums(limit)
    for a in range(2, n):
        # Skip checked numbers
        if a in checked:
            continue
        # Check amicable
        b = proper_factor_sums[a]
        if proper_factor_sums[b] == a and a != b:
            amicable_sum += a + b
        checked.add(a)
        checked.add(b)
    return amicable_sum
