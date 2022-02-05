from utils.div import get_num_divisors
from utils.primes import get_primes


def get_high_divisible_tri_num(m: int) -> int:
    """Get the first triangle number with m <= 500 divisors."""
    if m > 500:
        raise ValueError("m > 500")
    primes = get_primes(10000)
    n = 0
    num_div = 0
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
