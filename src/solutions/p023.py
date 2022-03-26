from utils.div import sum_proper_factors


def get_abundant_nums(n: int) -> list[int]:
    """
    Get a set of abundant numbers less than n.
    (The sum of an abundant number's proper factors is greater than itself.)
    """
    return [i for i in range(12, n + 1) if sum_proper_factors(i) > i]


def get_non_sum_two_abundant():
    """
    Get the sum of all positive integers which cannot be written as the
    sum of two abundant numbers.
    """
    ubound = 28123
    abundant_nums = get_abundant_nums(ubound)
    # Get sum of numbers which are NOT a sum of two abundant numbers
    sta = set()
    for i, a in enumerate(abundant_nums):
        for b in abundant_nums[i:]:
            ab_sum = a + b
            if ab_sum > ubound:
                break
            sta.add(ab_sum)
    return sum(x for x in range(1, ubound) if x not in sta)
