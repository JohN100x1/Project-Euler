from collections import defaultdict

from utils.exceptions import SolutionNotFoundError


def get_digit_tuple(n: int) -> tuple[int, ...]:
    """Get a 10-tuple of the digits of n."""
    y = n
    dlist = [0] * 10
    while y != 0:
        d = y % 10
        dlist[d] += 1
        y //= 10
    return tuple(dlist)


def get_smallest_cube_with_five_perms() -> int:
    """Get the smallest cube with 5 permutations that are also cube."""
    tuples = defaultdict(set)
    max_n = 10000
    for n in range(max_n):
        cube = n**3
        tup = get_digit_tuple(cube)
        tuples[tup].add(cube)
        if len(tuples[tup]) == 5:
            return min(tuples[tup])
    raise SolutionNotFoundError(f"No solution for n<{max_n}.")
