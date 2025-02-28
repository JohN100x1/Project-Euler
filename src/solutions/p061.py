from collections import defaultdict
from typing import Callable


def get_set_poly_nums(poly: Callable[[int], int]) -> dict[int, set[int]]:
    """
    Get a dict of 4-digit integers from poly which are split into two
    2-digit-cyclic parts.
    """
    nums = defaultdict(set)
    n = 1
    nth_term = poly(n)
    while nth_term < 10**4:
        half2 = nth_term % 100
        if nth_term >= 10**3 and half2 >= 10:
            half1 = (nth_term - half2) // 100
            nums[half1].add(half2)
        n += 1
        nth_term = poly(n)
    return nums


class PolygonalSearch:
    """
    Search for six 2-digit-cyclic 4-digit numbers where each are in each
    Polygonal: triangle, square, pentagonal, hexagonal, heptagonal, octagonal.
    """

    def __init__(self) -> None:
        self.cyclic_polys: list[list[int]] = []
        self.poly_funcs = [
            lambda n: n * (n + 1) // 2,
            lambda n: n**2,
            lambda n: n * (3 * n - 1) // 2,
            lambda n: n * (2 * n - 1),
            lambda n: n * (5 * n - 3) // 2,
            lambda n: n * (3 * n - 2),
        ]
        self.poly_nums: list[dict[int, set[int]]] = []

    def dfs_cyclic_polygonal_nums(
        self, chain: list[int], poly: list[int]
    ) -> None:
        """Depth first search for 2-digit-cyclic 4-digit polygonal numbers."""
        last_idx = poly[-1]
        depth = len(chain) - 1
        if depth == 5:
            if chain[0] in self.poly_nums[last_idx][chain[-1]]:
                self.cyclic_polys.append(chain + [chain[0]])
            return
        for i in range(len(self.poly_nums)):
            if i in poly:
                continue
            new_poly = poly + [i]
            for half2 in self.poly_nums[last_idx][chain[-1]]:
                if half2 in self.poly_nums[i]:
                    new_chain = chain + [half2]
                    self.dfs_cyclic_polygonal_nums(new_chain, new_poly)

    def sum_cyclic_polygonal_nums(self) -> int:
        """Get the sum of the six 2-digit-cyclic 4-digit polygonal numbers."""
        self.poly_nums = [get_set_poly_nums(func) for func in self.poly_funcs]

        # Try DFS starting points in each type of polygon
        for i in range(len(self.poly_nums)):
            for v in self.poly_nums[i]:
                self.dfs_cyclic_polygonal_nums([v], [i])
            if len(self.cyclic_polys) > 0:
                break

        tens_sum = sum(tens for tens in self.cyclic_polys[0][:-1])
        hund_sum = sum(hund for hund in self.cyclic_polys[0][1:])
        poly_sum = tens_sum + 100 * hund_sum

        return poly_sum
