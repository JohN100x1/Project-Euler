def get_partition_count(n):
    plist = [1, 1]
    for x in range(2, n+1):
        psum = 0
        sqrt1p24x = (1+24*x)**0.5
        for k in range(1, int(1+sqrt1p24x)//6+1):
            psum += (-1)**(k+1)*plist[x-k*(3*k-1)//2]
        for k in range(1, int(-1+sqrt1p24x)//6+1):
            psum += (-1)**(k+1)*plist[x-k*(3*k+1)//2]
        plist.append(psum)
    return plist[n]-1

print(get_partition_count(100))