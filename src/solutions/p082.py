import numpy as np

from config import path_res


def load_matrix() -> np.array:
    """Load the matrix of integers from /res/p081_matrix.txt"""
    path_txt = path_res / "p081_matrix.txt"
    return np.loadtxt(path_txt, dtype=np.int32, delimiter=",")


def get_three_way_min_path_sum(matrix: np.array) -> int:
    """
    Get the minimum path sum going only UP, DOWN and RIGHT starting left.

    Source: https://projecteuler.net/thread=82;page=2#5608
    """
    opt = [[row[0]] for row in matrix]
    for col in range(1, len(matrix[0])):
        for row in range(len(matrix)):
            opt[row].append(matrix[row][col] + opt[row][col - 1])

        for row in range(1, len(matrix)):
            if opt[row - 1][col] + matrix[row][col] < opt[row][col]:
                opt[row][col] = opt[row - 1][col] + matrix[row][col]

        for row in reversed(range(len(matrix) - 1)):
            if opt[row + 1][col] + matrix[row][col] < opt[row][col]:
                opt[row][col] = opt[row + 1][col] + matrix[row][col]

    return min(row[-1] for row in opt)
