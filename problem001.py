def get_35sum(n: int) -> int:
    n3 = (n-1) // 3
    n5 = (n-1) // 5
    n15 = (n-1) // 15
    s = 0.5*(3*n3*(n3+1)+5*n5*(n5+1)-15*n15*(n15+1))
    return int(s)

print(get_35sum(1000))