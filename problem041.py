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

def perm_last(dlist, k):
    # return highest in order
    if k == 1 or len(dlist) == 1:
        return [dlist]
    else:
        perms = []
        for d in sorted(dlist[-k:])[::-1]:
            dlist2 = dlist.copy()
            dlist2.remove(d)
            dlist2.insert(1-k, d)
            for perm in perm_last(dlist2, k-1):
                perms.append(perm)
        return perms

def get_max_pandigital_prime():
    # 1-8 and 1-9 pandigitals are not prime
    # because the sum of their digits are divisible by 3
    for k in range(7, 0, -1):
        dlist = list(range(k,0,-1))
        perms = perm_last(dlist, k)
        for perm in perms:
            p = sum(d*10**i for i, d in enumerate(perm[::-1]))
            if is_prime(p):
                break
        else:
            continue
        break
    return p

print(get_max_pandigital_prime())