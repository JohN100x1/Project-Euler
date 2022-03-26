from utils.div import get_num_divisors


def get_high_divisible_tri_num(m: int) -> int:
    """Get the first triangle number with m divisors."""
    n = 0
    num_div = 0
    while num_div <= m:
        n += 1
        if n % 2 == 0:
            num_div1 = get_num_divisors(n // 2)
            num_div2 = get_num_divisors(n + 1)
        else:
            num_div1 = get_num_divisors(n)
            num_div2 = get_num_divisors((n + 1) // 2)
        num_div = num_div1 * num_div2
    return n * (n + 1) // 2
