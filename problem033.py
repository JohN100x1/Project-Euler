import numpy as np

def find_digit_cancel_frac():
    digit_fracs = set()
    for d in range(10, 100):
        for n in range(10, d):
            A = set(int(x) for x in str(n))
            B = set(int(x) for x in str(d))
            C = A & B
            # Skip Trivial examples and non-examples
            if 0 in C or len(C) != 1:
                continue
            (c, ) = C
            alist = list(int(x) for x in str(n))
            blist = list(int(x) for x in str(d))
            alist.remove(c)
            blist.remove(c)
            # Avoid zero div
            if blist[0] == 0:
                continue
            # Check if cancellation is correct
            if alist[0] / blist[0] == n / d:
                digit_fracs.add((n, d))
    numer = np.prod(list(x[0] for x in digit_fracs))
    denom = np.prod(list(x[1] for x in digit_fracs))
    simple_denom = denom // np.gcd(numer,denom)
    return simple_denom

print(find_digit_cancel_frac())