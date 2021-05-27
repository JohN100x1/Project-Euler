def find_35sum(n):
    n3 = n // 3
    n5 = n // 5
    n15 = n // 15
    if n3*3 == n:
        n3 -= 1
    if n5*5 == n:
        n5 -= 1
    if n15*15 == n:
        n15 -= 1
    s = 0.5*(3*n3*(n3+1)+5*n5*(n5+1)-15*n15*(n15+1))
    return s