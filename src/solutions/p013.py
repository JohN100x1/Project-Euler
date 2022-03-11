import numpy as np

from config import path_res


def load_nums() -> np.array:
    """Load an array of large numbers from /res/p013_numbers.txt."""
    return np.loadtxt(path_res / "p013_numbers.txt")


def get_first_ten_digits(nums: np.array) -> int:
    """Get first ten digits of list of large numbers."""

    ftd = np.sum(nums)
    ftd = int(str(ftd).replace(".", "")[:10])
    return ftd
