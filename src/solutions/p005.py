from math import gcd


def get_lcm(n: int) -> int:
    """Get the lowest common multiple of 1, 2, ..., n."""
    lcm = 1
    for i in range(1, n + 1):
        lcm *= i // gcd(lcm, i)
    return lcm
