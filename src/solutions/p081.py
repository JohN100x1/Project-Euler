import numpy as np
import numpy.typing as npt
from requests import get


def load_matrix() -> npt.NDArray[np.int32]:
    """Load the matrix of integers from p081_matrix.txt"""
    url = "https://projecteuler.net/project/resources/p081_matrix.txt"
    content = get(url).content.decode("utf-8").rstrip("\n").replace(",", " ")
    return np.fromstring(content, dtype=np.int32, sep="\n").reshape(80, 80)


def get_two_way_min_path_sum(matrix: npt.NDArray[np.int32]) -> int:
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
    return int(path_sums1[0])
