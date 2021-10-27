def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_first_side_length_prime_sub_ratio(ratio):
    pnum = 0
    total = 1
    for x in range(1, 100000):
        fourx2p1 = 4*x**2+1
        for diag in range(fourx2p1-2*x, fourx2p1+4*x+1, 2*x):
            if is_prime(diag):
                pnum += 1
        total += 4
        if pnum/total < ratio:
            return 2*x+1
    return pnum/total

print(get_first_side_length_prime_sub_ratio(0.1))