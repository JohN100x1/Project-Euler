def bin_boundary(m):
    return 9*m*10**(m-1)

def find_digit_bin(n):
    m = 1
    while n > bin_boundary(m):
        n -= bin_boundary(m)
        m += 1
    return m, n

def champernowne_digit(n):
    # Single digit case
    if n < 10:
        return n
    m, n = find_digit_bin(n)
    r = n % m
    if r == 0:
        return (n//m - 1) % 10
    elif r == 1:
        return (n//(m*10**(m-r))+1) % 10
    else:
        return (n//(m*10**(m-r))) % 10

def champernowne_product(nlist):
    product = 1
    for n in nlist:
        product *= champernowne_digit(n)
    return product

print(champernowne_product([10**k for k in range(1,7)]))