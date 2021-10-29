def get_sqrt_period(n):
    idx = 0
    qr = {}
    
    sqrtn = n**0.5
    a = int(sqrtn)
    T = sqrtn - a
    q = -a
    r = 1
    
    period = None
    while period is None:
        a = int(1/T)
        q, r = -q-(a*(n-q**2)//r), (n-q**2)//r
        if a not in qr:
            qr[a] = {(q,r):idx}
        else:
            if (q,r) in qr[a]:
                period = idx - qr[a][(q,r)]
            qr[a][(q,r)] = idx
        idx += 1
        T = (sqrtn + q)/r
    return period

def get_odd_sqrt_periods(N):
    count = 0
    for n in range(N+1):
        if int(n**0.5) != n**0.5:
            period = get_sqrt_period(n)
            if period % 2 == 1:
                count += 1
    return count

print(get_odd_sqrt_periods(10000))