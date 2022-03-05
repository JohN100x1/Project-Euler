import numpy as np

from config import path_res


def get_first_ten_digits() -> int:
    """Get first ten digits of list of large numbers."""

    numbers = np.loadtxt(path_res / "p013_numbers.txt")

    ftd = np.sum(numbers)
    ftd = int(str(ftd).replace(".", "")[:10])
    return ftd


print(get_first_ten_digits())
