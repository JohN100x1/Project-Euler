from utils.div import sum_proper_factors


def sum_amicable(n: int) -> int:
    """Get the sum of amicable numbers less than n."""
    checked = set()
    amicable_sum = 0
    for a in range(2, n):
        # Skip checked numbers
        if a in checked:
            continue
        # Check amicable
        b = sum_proper_factors(a)
        if sum_proper_factors(b) == a and a != b:
            amicable_sum += a + b
        checked.add(a)
        checked.add(b)
    return amicable_sum
