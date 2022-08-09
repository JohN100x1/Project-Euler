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
    pairs_to_check = [
        (0, 1),
        (0, 4),
        (0, 9),
        (1, 6),
        (2, 5),
        (3, 6),
        (4, 9),
        (6, 4),
        (8, 1),
    ]
    aug_a = set_a | {6, 9} if 6 in set_a or 9 in set_a else set_a
    aug_b = set_b | {6, 9} if 6 in set_b or 9 in set_b else set_b
    for x, y in pairs_to_check:
        if not (x in aug_a and y in aug_b or y in aug_a and x in aug_b):
            return False
    return True
