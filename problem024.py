def sort_perm(x: str) -> list:
    if len(x) == 2:
        # Two-digit case
        if x[0] > x[1]:
            return [x[::-1], x]
        else:
            return [x, x[::-1]]
    else:
        digits = sorted(x)
        l = []
        for d in digits:
            other_digits = "".join([x for x in digits if x != d])
            l += [d+y for y in sort_perm(other_digits)]
        return l

print(sort_perm("0123456789")[999999])