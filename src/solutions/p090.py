from itertools import combinations


def count_cube_digit_pairs() -> int:
    """
    Get the number of distinct arrangements of 2 cubes that allow all
    squares below 100 to be displayed.
    """
    solutions = set()
    for i, cube_1 in enumerate(combinations(range(10), 6)):
        for j, cube_2 in enumerate(combinations(range(10), 6)):
            if i < j:
                break
            if is_possible(set(cube_1), set(cube_2)):
                solutions.add(tuple(sorted([cube_1, cube_2])))
    return len(solutions)


def is_possible(set_a: set[int], set_b: set[int]) -> bool:
    """Checks whether the two sets of 6 digits can form all squares."""
    six_nine_in_a = 6 in set_a or 9 in set_a
    six_nine_in_b = 6 in set_b or 9 in set_b
    if not (0 in set_a and 1 in set_b or 1 in set_a and 0 in set_b):
        return False
    if not (0 in set_a and 4 in set_b or 4 in set_a and 0 in set_b):
        return False
    if not (0 in set_a and six_nine_in_b or six_nine_in_a and 0 in set_b):
        return False
    if not (1 in set_a and six_nine_in_b or six_nine_in_a and 1 in set_b):
        return False
    if not (2 in set_a and 5 in set_b or 5 in set_a and 2 in set_b):
        return False
    if not (3 in set_a and six_nine_in_b or six_nine_in_a and 3 in set_b):
        return False
    if not (4 in set_a and six_nine_in_b or six_nine_in_a and 4 in set_b):
        return False
    if not (six_nine_in_a and 4 in set_b or 4 in set_a and six_nine_in_b):
        return False
    if not (8 in set_a and 1 in set_b or 1 in set_a and 8 in set_b):
        return False
    return True
