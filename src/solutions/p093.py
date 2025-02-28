from itertools import combinations
from typing import Generator


def generate_abcd() -> Generator[set[int], None, None]:
    """Generate digits a < b < c < d."""
    for d in range(4, 10):
        for c in range(3, d):
            for b in range(2, c):
                for a in range(1, b):
                    yield {a, b, c, d}


def explore_arth_ops(num1: float, num2: float) -> list[float]:
    """Explore all 4 arithmetic operations and return the results."""
    results = [num1 + num2, num1 - num2, num2 - num1, num1 * num2]
    if num1 != 0:
        results.append(num2 / num1)
    if num2 != 0:
        results.append(num1 / num2)
    return results


def get_consecutive_target_set(abcd: set[int]) -> int:
    """
    Return the max of consecutive integer targets 1 to n that could be created
    from a < b < c < d.
    """
    targets = set()
    for digits in combinations(abcd, 2):
        # Once two digits are operated on, only need to consider the
        # composition order of the remaining two digits.
        # NOTE: Compositions like x1 o ((x2 o x3) o x4) will already be
        #       captured by ((x1 o x2) o x3) o x4 because all initial pair
        #       composition combinations are considered.
        #       i.e. x1 = 4, x2 = 1, x3 = 2, x4 = 3 in the first case is
        #            x1 = 1, x2 = 2, x3 = 3, x4 = 4 in the second case
        # The compositions to consider are listed below
        results1 = set()  # ((x1 o x2) o x3) o x4
        results2 = set()  # ((x1 o x2) o x4) o x3
        ________ = set()  # (x1 o x2) o (x3 o x4)

        remaining = tuple(abcd - set(digits))
        x1_x2_comp = explore_arth_ops(digits[0], digits[1])
        x3_x4_comp = explore_arth_ops(remaining[0], remaining[1])
        for num1 in x1_x2_comp:
            results1.update(explore_arth_ops(num1, remaining[0]))
            results2.update(explore_arth_ops(num1, remaining[1]))
            for num2 in x3_x4_comp:
                targets.update(explore_arth_ops(num1, num2))

        for num in results1:
            targets.update(explore_arth_ops(num, remaining[1]))

        for num in results2:
            targets.update(explore_arth_ops(num, remaining[0]))

    max_consecutive_target = 0
    for num in range(1, len(targets)):
        if num in targets:
            max_consecutive_target += 1
        else:
            return max_consecutive_target
    return max_consecutive_target


def get_max_consecutive_target_abcd() -> int:
    max_abcd = 0
    max_consecutive_target = 0
    for abcd in generate_abcd():
        consecutive_target = get_consecutive_target_set(abcd)
        if consecutive_target > max_consecutive_target:
            max_abcd = int("".join(str(x) for x in sorted(abcd)))
            max_consecutive_target = consecutive_target
    return max_abcd
