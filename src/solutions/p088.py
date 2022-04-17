from copy import copy
from math import prod

from utils.primes import get_primes


def get_prime_factorisation(n: int, primes: list[int]) -> list[int]:
    """Get a list of the prime factors of n > 0."""
    factors = []
    if n <= 0:
        raise ValueError(f"n={n} out of range. Choose n > 0.")
    for prime in primes:
        while n % prime == 0:
            n //= prime
            factors.append(prime)
        if n == 1:
            break
    else:
        raise ValueError("Not enough primes to completely factor n.")
    return factors


def get_sub_prod_partitions(factors: list[int]) -> set[tuple[int, ...]]:
    """
    Get sub product partitions of n with at least two partitions.
    >>> get_sub_prod_partitions([2,3,5])
    {(2, 15), (3, 10), (5, 6), (2, 3, 5)}
    """
    if len(factors) <= 2:
        return {tuple(sorted(factors))}

    new_factors = copy(factors)
    last_factor = new_factors.pop()
    partitions = {tuple(sorted((int(prod(new_factors)), last_factor)))}
    for partition in get_sub_prod_partitions(new_factors):
        partitions.add(tuple(sorted(partition + (last_factor,))))
        for idx in range(len(partition)):
            part = list(partition)
            part[idx] *= last_factor
            partitions.add(tuple(sorted(part)))
    return partitions


def sum_min_prod_sum_num(max_k: int) -> int:
    """
    Get the sum of the minimum n = prod(S(k)) = sum(S(k)) where S(k) is a
    set of k numbers between 2 <= k <= max_k.

    Fact: n = prod(S(k)) = sum(S(k)) > k.
    Fact: n is not prime.
    """
    primes = get_primes(2 * max_k)
    prime_set = set(primes)
    k_min_nums = {}
    n = 4
    last_k = 1
    while last_k < max_k:
        # primes don't have proper prime factors
        if n in prime_set:
            n += 1
            continue

        # Get all possible k from fixed n, set as min n for k if k isn't set.
        factors = get_prime_factorisation(n, primes)
        for comb in get_sub_prod_partitions(factors):
            k = n - sum(comb) + len(comb)
            if k not in k_min_nums:
                k_min_nums[k] = n

        # Update the last consecutive k seen. (we want no gaps.)
        while last_k + 1 in k_min_nums:
            last_k += 1
        n += 1

    return sum(set(v for k, v in k_min_nums.items() if k <= max_k))
