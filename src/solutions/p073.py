def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_frac_count(N=12000):
    count = 0
    for d in range(2, N+1):
        for n in range(d//3,d//2+1):
            if d < 3*n and 2*n < d and gcd(n, d) == 1:
                count += 1
    return count

print(get_frac_count(12000))