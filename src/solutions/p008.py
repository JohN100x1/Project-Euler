from config import path_res


def get_largest_product(d: int) -> int:
    """Get the largest product of d adjacent digits in string"""

    # Read from file
    with open(path_res / "p008_digits.txt") as f:
        str_digits = f.read().replace("\n", "")

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
