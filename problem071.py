def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_max_numerator_37():
    max_n = 0
    max_nd = 0.0
    for d in range(10**6, 4, -1):
        for n in range((3*d-1)//7,(3*d)//7):
            if 7*n < 3*d and gcd(n, d) == 1:
                if n/d > max_nd:
                    max_n = n
                    max_nd = n/d
    return max_n

print(get_max_numerator_37())