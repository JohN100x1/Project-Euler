def ulam_spiral_diag_sum(n):
    # https://www.desmos.com/calculator/eqr1s8kxcn
    S = (n+1)*(4*n**2-n+9)//6-3
    return S

print(ulam_spiral_diag_sum(1001))