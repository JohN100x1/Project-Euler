from utils.exceptions import SolutionNotFoundError


def get_permuted_multiples(n: int, max_d: int = 10) -> int:
    """
    Get the smallest number x such that for 1, 2, ..., n,
    n * x is a permutation of the digits of x.

    max_d determines the maximum number of digits x can have.
    """
    for d in range(max_d):
        for x in range(10 ** (d + 1) // n, 10**d, -1):
            digits = sorted(str(x))
            for m in range(1, n + 1):
                if digits != sorted(str(m * x)):
                    break
            else:
                return x
    raise SolutionNotFoundError(f"No solution for d<{max_d}.")
