def get_permuted_multiples(coeffs):
    for d in range(len(coeffs)):
        lbound = 10**d
        ubound = 10**(d+1)//6
        for x in range(lbound, ubound):
            digits = sorted(str(x))
            for m in coeffs:
                if digits != sorted(str(m*x)):
                    break
            else:
                return x
    return None

print(get_permuted_multiples([1,2,3,4,5,6]))