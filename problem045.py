def find_TPH(N):
    c = None
    for a in range(144, N):
        b = (1+(1+24*a*(2*a-1))**0.5)/6
        if int(b) == b:
            c = 2*a - 1
            Tc = c*(c+1)//2
    return Tc

print(find_TPH(100000))