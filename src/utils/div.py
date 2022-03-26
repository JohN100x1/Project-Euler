from collections import defaultdict

from config import PRIMES


def get_num_divisors(n: int) -> int:
    """
    Get the number of divisors of an integer n > 0.

    >>> get_num_divisors(45)
    6
    """
    num_div = 1
    if n <= 0:
        raise ValueError(f"n={n} out of range. Choose n > 0.")
    for prime in PRIMES:
        power = 1
        while n % prime == 0:
            n //= prime
            power += 1
        num_div *= power
        if n in {1, -1}:
            break
    return num_div


def get_prime_factorisation(n: int) -> dict[int, int]:
    """
    Get the prime factorisation of an integer n > 0.

    >>> get_prime_factorisation(180)
    {2: 2, 3: 2, 5: 1}
    """
    products = defaultdict(int)
    if n <= 0:
        raise ValueError(f"n={n} out of range. Choose n > 0.")
    for prime in PRIMES:
        while n % prime == 0:
            n //= prime
            products[prime] += 1
        if n in {1, -1}:
            break
    return dict(products)


def sum_factors(n: int) -> int:
    """
    Get the sum of the factors of an integer n > 0.

    >>> sum_factors(192)
    508
    """
    factor_sum = 1
    prime_factors = get_prime_factorisation(n)
    for p, exp in prime_factors.items():
        factor_sum *= (p ** (exp + 1) - 1) // (p - 1)
    return factor_sum


def sum_proper_factors(n: int) -> int:
    """
    Get the sum of the proper factors of an integer n > 0.

    >>> sum_proper_factors(192)
    316
    """
    return sum_factors(n) - n
