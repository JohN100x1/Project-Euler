def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def get_digit_cancel_frac():
    digits = {1,2,3,4,5,6,7,8,9}
    dfracs = set()
    for a in digits:
        for b in digits - {a}:
            for c in digits - {a, b}:
                # Check only fractions < 1
                if b > c:
                    continue
                # Case 1: ab / ac = b / c
                # Which is only true when b = c
                
                # Case 2: ab / ca = b / c
                if (10*a+b)*c == b*(10*c+a):
                    dfracs.add((10*a+b, 10*c+a))
                # Case 3: ba / ac = b / c
                if (10*b+a)*c == b*(10*a+c):
                    dfracs.add((10*b+a, 10*a+c))
                
                # Case 4: ba / ca = b / c
                # Which is only true when b = c
    numer, denom = 1, 1
    for n, d in dfracs:
        numer *= n
        denom *= d
    simple_denom = denom // gcd(numer, denom)
    return simple_denom

print(get_digit_cancel_frac())