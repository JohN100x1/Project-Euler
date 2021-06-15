def is_pandigital(dlist: list) -> bool:
    is_pd = True
    # Check no repeats
    if len(set(dlist)) != len(dlist):
        is_pd = False
    # Check set is equal
    if set(dlist) != set(range(1,10)):
        is_pd = False
    return is_pd

def find_largest_pandigital_multiple():
    pandigitals = set()
    for x in range(1,9999):
        multiple = 1
        digits = []
        while len(digits) < 9:
            product = x * multiple
            digits += [int(d) for d in str(product)]
            multiple += 1
        if len(digits) > 9:
            continue
        if is_pandigital(digits):
            pandigitals.add(int("".join(str(d) for d in digits)))
    return max(pandigitals)

print(find_largest_pandigital_multiple())