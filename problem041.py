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
        return dlist
    elif k == 2:
        if dlist[-1] < dlist[-2]:
            new_dlist2 = dlist.copy()
            new_dlist2[-1], new_dlist2[-2] = new_dlist2[-2], new_dlist2[-1]
            return dlist, new_dlist2
        else:
            new_dlist1 = dlist.copy()
            new_dlist1[-1], new_dlist1[-2] = new_dlist1[-2], new_dlist1[-1]
            return new_dlist1, dlist
    else:
        new_dlists = []
        for d in sorted(dlist[-k:])[::-1]:
            fixed_dlist = dlist.copy()
            fixed_dlist.remove(d)
            fixed_dlist.insert(1-k,d)
            for new_dlist in perm_last(fixed_dlist, k-1):
                new_dlists.append(new_dlist)
        return new_dlists

def find_largest_pandigital_prime():
    is_p = False
    for k in range(9, 0, -1):
        dlist = list(range(k,0,-1))
        perms = perm_last(dlist, k)
        for perm in perms:
            p = int("".join(str(d) for d in perm))
            if is_prime(p):
                is_p = True
                break
        if is_p == True:
            break
    return p

print(find_largest_pandigital_prime())