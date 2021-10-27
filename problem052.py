def search_permuted_multiples(max_digits=6):
    for d in range(max_digits):
        lbound = 10**d
        ubound = 10**(d+1)//6
        for x in range(lbound, ubound):
            digits = sorted(str(x))
            for m in range(1, 7):
                if digits != sorted(str(m*x)):
                    break
            else:
                return x
    return None

print(search_permuted_multiples())