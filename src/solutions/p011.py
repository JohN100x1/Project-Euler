import numpy as np

from config import path_res


def get_largest_prod() -> int:

    # Load from file
    grid = np.loadtxt(path_res / "p011_grid.txt", dtype=np.int64)

    max_product = 1
    n = grid.shape[0]

    # row product
    for i in range(n):
        for j in range(n - 4):
            p = np.prod(grid[i, j : j + 4])
            if p >= max_product:
                max_product = p

    # column product
    for i in range(n - 4):
        for j in range(n):
            p = np.prod(grid[i : i + 4, j])
            if p >= max_product:
                max_product = p
    dx = np.array([0, 1, 2, 3])

    # left diagonal product
    for i in range(n - 4):
        for j in range(n - 4):
            p = np.prod(grid[i + dx, j + dx])
            if p >= max_product:
                max_product = p

    # right diagonal product
    for i in range(3, n):
        for j in range(n - 4):
            p = np.prod(grid[i - dx, j + dx])
            if p >= max_product:
                max_product = p
    return max_product
