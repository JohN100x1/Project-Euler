import numpy as np

from utils.primes import get_primes


def get_longest_prime_sum(n: int) -> int:
    primes = get_primes(10**6)
    prime_set = set(primes)
    p_sums1 = np.cumsum(primes)
    p_sums2 = np.zeros(len(p_sums1) + 1, dtype="int32")
    p_sums2[1:] = p_sums1
    # The sum of the First 547 primes >1 million
    for L in range(546, 0, -1):
        j = 0
        p_sum = p_sums1[L + j] - p_sums2[j]
        while p_sum < n:
            if p_sum in prime_set:
                return p_sum
            j += 1
            p_sum = p_sums1[L + j] - p_sums2[j]
