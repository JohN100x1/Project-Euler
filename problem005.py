def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def smallest_lcm(n):
    lcm = 1
    for i in range(1,n+1):
        lcm = lcm*i//gcd(lcm, i)
    return lcm

print(smallest_lcm(20))