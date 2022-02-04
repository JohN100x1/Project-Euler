def get_sqrt_seq(n, seqlen):
    assert(int(n**0.5) != n**0.5)
    idx = 0
    sqrtn = n**0.5
    seq = [int(sqrtn)]
    a = seq[0]
    T = sqrtn - a
    q = -a
    r = 1
    
    for i in range(seqlen-1):
        a = int(1/T)
        q, r = -q-(a*(n-q**2)//r), (n-q**2)//r
        seq.append(a)
        idx += 1
        T = (sqrtn + q)/r
    return seq

def get_sqrt_convergent(n, seqlen):
    sqrt_seq = get_sqrt_seq(n, seqlen)
    denom = 1
    numer = sqrt_seq[seqlen-1]
    for k in range(2, seqlen+1):
        numer, denom = numer*sqrt_seq[seqlen-k]+denom, numer
    return (numer, denom)

def get_max_diophantine():
    max_d = 0
    max_x = 0
    for D in range(2, 1001):
        if D**0.5 == int(D**0.5):
            continue
        i = 0
        x, y = get_sqrt_convergent(D, i)
        while x**2 - D*y**2 != 1:
            i += 1
            x, y = get_sqrt_convergent(D, i)
        if x > max_x:
            max_x = x
            max_d = D
    return max_d

print(get_max_diophantine())