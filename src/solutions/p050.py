import numpy as np

from config import PRIME_SET, PRIMES


def get_longest_prime_sum(n: int) -> int:
    p_sums1 = np.cumsum(PRIMES)
    p_sums2 = np.zeros(len(p_sums1) + 1, dtype="int32")
    p_sums2[1:] = p_sums1
    # The sum of the First 547 primes >1 million
    for L in range(546, 0, -1):
        j = 0
        p_sum = p_sums1[L + j] - p_sums2[j]
        while p_sum < n:
            if p_sum in PRIME_SET:
                return p_sum
            j += 1
            p_sum = p_sums1[L + j] - p_sums2[j]
