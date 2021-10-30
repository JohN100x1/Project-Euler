with open("p008_digits.txt") as f:
    DIGITS = f.read().replace("\n","")

def get_largest_product(d: int) -> int:
    N = len(DIGITS) - (d-1)
    product = 1
    idx = 0
    while idx <= N:
        nums = DIGITS[idx:idx+d]
        p = 1
        for i, n in enumerate(nums):
            if n == "0":
                idx += d-i
                break
            else:
                p *= int(n)
        else:
            idx += 1
            if p >= product:
                product = p
    return product

print(get_largest_product(13))