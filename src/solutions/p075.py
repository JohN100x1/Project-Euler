def get_unique_L_triple_count(N):
    family = set()
    checked = set()
    Lcounts = {}
    for x in range(2, N):
        for y in range(1, x):
            a = x**2 - y**2
            b = 2*x*y
            c = x**2 + y**2
            if a > b:
                a, b = b, a
            if (a/c, b/c) not in family:
                n = 1
                L = a + b + c
                if L > N:
                    break
                dL = L
                # Whole multiple
                while L <= N:
                    sol = (a*n, b*n, c*n)
                    if sol in checked:
                        n += 1
                        L += dL
                        continue
                    if L not in Lcounts:
                        Lcounts[L] = 1
                    else:
                        Lcounts[L] += 1
                    checked.add(sol)
                    n += 1
                    L += dL
                family.add((a/c, b/c))
    return sum(1 for l, v in Lcounts.items() if v == 1)

print(get_unique_L_triple_count(1500000))