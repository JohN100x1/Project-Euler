import numpy as np
import numpy.typing as npt

from config import path_res


def load_grid() -> npt.NDArray[np.int64]:
    """Load grid of integers from /res/p011_grid.txt"""
    return np.loadtxt(path_res / "p011_grid.txt", dtype=np.int64)


def get_largest_prod(grid: npt.NDArray[np.int64]) -> int:
    """Get the largest product of 4 numbers in line on the grid."""

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

    # left diagonal product
    dx = np.array([0, 1, 2, 3])
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
