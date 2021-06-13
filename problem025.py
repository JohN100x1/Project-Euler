def nth_fibonacci_digits(d):
    if d == 1:
        return 1
    Fm = 1
    Fn = 1
    n = 2
    while len(str(Fn)) < d:
        Fn, Fm = Fn + Fm, Fn
        n += 1
    return n
    
print(nth_fibonacci_digits(1000))