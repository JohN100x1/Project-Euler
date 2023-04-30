from re import findall

import numpy as np
import numpy.typing as npt
from requests import get


def load_nums() -> npt.NDArray[np.float64]:
    """Load array of large numbers from https://projecteuler.net/problem=13."""
    url = "https://projecteuler.net/problem=13"
    content = get(url).content.decode("utf-8")
    nums = "\n".join(findall(r"\n(\d+)<br />", content))
    return np.fromstring(nums, sep="\n", dtype=np.float64)


def get_first_ten_digits(nums: npt.NDArray[np.float64]) -> int:
    """Get first ten digits of list of large numbers."""

    ftd = np.sum(nums)
    return int(str(ftd).replace(".", "")[:10])
