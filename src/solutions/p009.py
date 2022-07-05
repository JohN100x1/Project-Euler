from utils.exceptions import SolutionNotFoundError


def get_pytriple_prod(n: int) -> int:
    """Get abc such that a^2+b^2=c^2 and a+b+c=n."""
    for a in range(1, n // 2 + 1):
        numerator = n**2 // 2 - n * a
        denominator = n - a
        if numerator % denominator == 0:
            b = numerator // denominator
            abc = a * b * (n - a - b)
            return abc
    raise SolutionNotFoundError("Failed to solve p009.")
