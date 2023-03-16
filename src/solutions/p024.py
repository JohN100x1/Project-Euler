from math import factorial


def get_nth_lexicographic_perm(dlist: list[int], n: int) -> int:
    """Get the n-th lexicographic permutation of dlist."""
    perm = 0
    r = n - 1
    for i in range(len(dlist) - 1, -1, -1):
        q, r = divmod(r, factorial(i))
        perm += pow(10, len(dlist) - 1) * dlist.pop(q)
    return perm
