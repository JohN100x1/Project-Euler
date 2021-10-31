def get_min_pentagonal_diff(N=3000):
    # https://www.desmos.com/calculator/q44wzac3qg
    # Generate Pentagonal numbers
    Pnums = {n*(3*n-1)//2 for n in range(1,int(1.5*N))}
    D = float("inf")
    for i in range(1, N+1):
        Pi = i*(3*i-1)//2
        for j in range(int((1+(72*i-47)**0.5)/6), i):
            Pj = j*(3*j-1)//2
            Psum = Pi + Pj
            Psub = Pi - Pj
            if Psum in Pnums and Psub in Pnums:
                if Psub < D:
                    D = Psub
    return D

print(get_min_pentagonal_diff())