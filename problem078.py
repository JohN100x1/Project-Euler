def get_partition_divisible_by(d, maxit=10**6):
    plist = [1, 1]
    for x in range(2, maxit+1):
        psum = 0
        sqrt1p24x = (1+24*x)**0.5
        for k in range(1, int(1+sqrt1p24x)//6+1):
            psum += (-1)**(k+1)*plist[x-k*(3*k-1)//2]
        for k in range(1, int(-1+sqrt1p24x)//6+1):
            psum += (-1)**(k+1)*plist[x-k*(3*k+1)//2]
        if psum % d == 0:
            return x
        plist.append(psum)
    return None

print(get_partition_divisible_by(10**6))