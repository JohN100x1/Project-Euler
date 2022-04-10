import numpy as np

from config import path_res


def load_matrix() -> np.array:
    """Load the matrix of integers from /res/p081_matrix.txt"""
    path_txt = path_res / "p081_matrix.txt"
    return np.loadtxt(path_txt, dtype=np.int32, delimiter=",")


def get_two_way_min_path_sum(matrix: np.array) -> int:
    """Get the minimum path sum going only RIGHT and DOWN starting top-left."""
    ubound = matrix.shape[0] + matrix.shape[1] - 2
    halfway = (matrix.shape[0] + matrix.shape[1]) // 2
    path_sums1 = [matrix[-1][-1]]
    for i in range(ubound, 0, -1):
        path_sums1, path_sums2 = [], path_sums1
        diagonal = np.diag(matrix[::-1, :], i - matrix.shape[0])
        limit = len(diagonal) - 1
        if i >= halfway:
            for j, n in enumerate(diagonal):
                if j == 0:
                    path_sum = diagonal[j] + path_sums2[j]
                elif j == limit:
                    path_sum = diagonal[j] + path_sums2[j - 1]
                else:
                    sum1 = diagonal[j] + path_sums2[j - 1]
                    sum2 = diagonal[j] + path_sums2[j]
                    path_sum = min(sum1, sum2)
                path_sums1.append(path_sum)
        else:
            for j, n in enumerate(diagonal):
                sum1 = diagonal[j] + path_sums2[j]
                sum2 = diagonal[j] + path_sums2[j + 1]
                path_sums1.append(min(sum1, sum2))
    return path_sums1[0]
