from math import factorial

def get_nth_lexicographic_perm(dlist, n):
    perm = 0
    r = n - 1
    for i in range(len(dlist)-1, -1, -1):
        q, r = r // factorial(i), r % factorial(i)
        perm += pow(10, len(dlist)-1)*dlist.pop(q)
    return perm

print(get_nth_lexicographic_perm([0,1,2,3,4,5,6,7,8,9], 1000000))