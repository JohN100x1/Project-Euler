from re import findall

from requests import get


def load_str_digits() -> str:
    """Load a string of digits 0-9 from https://projecteuler.net/problem=8."""
    url = "https://projecteuler.net/problem=8"
    content = get(url).content.decode("utf-8")
    return "".join(findall(r"\n(\d+)<br />", content))


def get_largest_product(d: int, str_digits: str) -> int:
    """Get the largest product of d adjacent digits in string."""

    # Calculate largest product
    max_idx = len(str_digits) - (d - 1)
    product = 1
    idx = 0
    while idx <= max_idx:
        nums = str_digits[idx : idx + d]
        p = 1
        for i, n in enumerate(nums):
            if n == "0":
                idx += d - i
                break
            else:
                p *= int(n)
        else:
            idx += 1
            if p >= product:
                product = p
    return product
