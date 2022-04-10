from utils.primes import get_primes


def get_num_divisors(n: int, primes: list[int]) -> int:
    """Get the number of divisors of an integer n > 0."""
    num_div = 1
    if n <= 0:
        raise ValueError(f"{n=} out of range. Choose n > 0.")
    for prime in primes:
        power = 1
        while n % prime == 0:
            n //= prime
            power += 1
        num_div *= power
        if n == 1:
            break
    else:
        raise ValueError(f"Not enough primes to work for {n=}")
    return num_div


def get_high_divisible_tri_num(m: int, p_limit=10**6) -> int:
    """Get the first triangle number with m divisors."""
    n = 0
    num_div = 0
    primes = get_primes(p_limit)
    while num_div <= m:
        n += 1
        if n % 2 == 0:
            num_div1 = get_num_divisors(n // 2, primes)
            num_div2 = get_num_divisors(n + 1, primes)
        else:
            num_div1 = get_num_divisors(n, primes)
            num_div2 = get_num_divisors((n + 1) // 2, primes)
        num_div = num_div1 * num_div2
    return n * (n + 1) // 2
