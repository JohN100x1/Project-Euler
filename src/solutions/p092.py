from collections import Counter
from itertools import combinations_with_replacement
from math import factorial, prod


def count_square_digit_chain():
    """Counts the number of sum of squared digits chains that end in 89."""
    total = 0

    digit_combinations = combinations_with_replacement(range(10), 7)
    next(digit_combinations)
    chain_1 = {1}
    chain_89 = {89}
    for digits in digit_combinations:
        sum_sqs = [sum(d**2 for d in digits)]
        while sum_sqs[-1] not in chain_1 and sum_sqs[-1] not in chain_89:
            sum_sq = sum_sqs[-1]
            new_sum_sq = 0
            while sum_sq > 0:
                new_sum_sq += (sum_sq % 10) ** 2
                sum_sq //= 10
            sum_sqs.append(new_sum_sq)
        if sum_sqs[-1] in chain_1:
            chain_1.update(sum_sqs)
            continue
        chain_89.update(sum_sqs)
        total += factorial(7) // prod(
            factorial(x) for x in Counter(digits).values()
        )
    return total
