import numpy as np
import numpy.typing as npt

from config import path_res


def load_nums() -> npt.NDArray[np.float64]:
    """Load an array of large numbers from /res/p013_numbers.txt."""
    return np.loadtxt(path_res / "p013_numbers.txt")


def get_first_ten_digits(nums: npt.NDArray[np.float64]) -> int:
    """Get first ten digits of list of large numbers."""

    ftd = np.sum(nums)
    return int(str(ftd).replace(".", "")[:10])
