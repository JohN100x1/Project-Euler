def get_next_TPH(n=143):
    # n is the n-th Hexagonal term
    a = n + 1
    while (1+24*a*(2*a-1))**0.5 % 6 != 5:
        a += 1
    c = 2*a-1
    Tc = c*(c+1)//2
    return Tc

print(get_next_TPH())