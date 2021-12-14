def sum_term(a_plus_b, c, n):
    return max((a_plus_b*n)//2 + 1 - max(a_plus_b*n - c*n, 1), 0)

def get_family_sol_count(family, a_plus_b, c, l, twoM, M):
    family_sol_count = 0
    if a_plus_b <= twoM and c <= M and (a_plus_b/l, c/l) not in family:
        nrange = range(1, min(twoM//a_plus_b, M//c)+1)
        family_sol_count += sum(sum_term(a_plus_b, c, n) for n in nrange)
        family.add((a_plus_b/l, c/l))
    return family_sol_count

def get_cuboid_sol_count(M):
    # Solve for integers l**2 = (a + b)**2 + c**
    # Where a <= b <= c
    sol_count = 0
    ubound = (M + M*(5**0.5/2))**0.5
    family = set()
    twoM = 2*M
    for x in range(2, int(ubound)+1):
        for y in range(1, x):
            a_plus_b = x**2 - y**2
            c = 2*x*y
            l = x**2 + y**2
            sol_count += get_family_sol_count(family, a_plus_b, c, l, twoM, M)
            sol_count += get_family_sol_count(family, c, a_plus_b, l, twoM, M)
    return sol_count

def get_M_with_cuboid_sol_count_greater_than(N):
    ### Do binary search here instead
    for M in range(1800, 2000):
        n = get_cuboid_sol_count(M)
        if n >= N:
            return M
    return None

print(get_M_with_cuboid_sol_count_greater_than(10**6))