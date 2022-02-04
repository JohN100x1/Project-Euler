DIGITS = {1,2,3,4,5,6,7,8,9}

def is_pandigital(dlist: list) -> bool:
    dset = set(dlist)
    # Check set contains all digits
    if dset != DIGITS:
        return False
    # Check no repeats
    if len(dset) != len(DIGITS):
        return False
    return True

def get_max_pandigital_concat():
    max_pandigital = 0
    # Starting number must have less than 4 digits
    # otherwise x * 1, x * 2, x * 3 has 12 digits
    ubound = pow(10, 4)
    for x in range(1, ubound):
        n = 1
        digits = []
        while len(digits) < 9:
            product = x * n
            digits += list(map(int, str(product)))
            n += 1
        if len(digits) > 9:
            continue
        if is_pandigital(digits):
            pandigital = int("".join(str(d) for d in digits))
            if pandigital > max_pandigital:
                max_pandigital = pandigital
    return max_pandigital

print(get_max_pandigital_concat())