def get_proper_factor_sums(n: int) -> list[int]:
    """Get a list of proper factor sums for all numbers less than n."""
    # Get the proper factor sums
    proper_factor_sums = [1] * n
    for i in range(2, int(n**0.5) + 1):
        proper_factor_sums[i * i] += i
        for k in range(i + 1, n // i + 1):
            proper_factor_sums[i * k] += i + k
    return proper_factor_sums


def get_non_sum_two_abundant(limit=28123):
    """
    Get the sum of all positive integers which cannot be written as the
    sum of two abundant numbers. Any integer bigger than 28123 can be written
    as a sum of two abundant numbers.
    """

    proper_factor_sums = get_proper_factor_sums(limit)

    ab_sum = 0
    abundant_nums = set()

    for i in range(1, limit):
        if proper_factor_sums[i] > i:
            abundant_nums.add(i)
        if not any(i - a in abundant_nums for a in abundant_nums):
            ab_sum += i
    return ab_sum
