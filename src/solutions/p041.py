from sympy import isprime


def perm_last(dlist: list[int], k: int) -> list[list[int]]:
    """Return a list of digit lists which permute the last k digits."""
    # return highest in order
    if k == 1 or len(dlist) == 1:
        return [dlist]
    else:
        perms = []
        for d in sorted(dlist[-k:], reverse=True):
            dlist2 = dlist.copy()
            dlist2.remove(d)
            dlist2.insert(1 - k, d)
            for perm in perm_last(dlist2, k - 1):
                perms.append(perm)
        return perms


def get_largest_pandigital_prime() -> int:
    """
    Get the largest pandigital prime.

    1-8 and 1-9 pandigital numbers are not prime
    because the sum of their digits are divisible by 3
    """
    for k in range(7, 0, -1):
        dlist = list(range(k, 0, -1))
        for perm in perm_last(dlist, k):
            p = sum(d * 10**i for i, d in enumerate(perm[::-1]))
            if isprime(p):
                return p
