def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10000)

def get_num_divisors(n: int) -> int:
    if n == 1:
        return 1
    else:
        dnum = 1
        sqrtn = int(n**0.5)+1
        for p in PRIMES:
            if p < sqrtn:
                power = 1
                while n % p == 0:
                    n //= p
                    power += 1
                dnum *= power
            else:
                break
        return dnum

def get_high_divisible_Tn(m: int) -> int:
    n = 0
    dnum = 0
    while dnum <= m:
        n += 1
        if n % 2 == 0:
            dnum1 = get_num_divisors(n//2)
            dnum2 = get_num_divisors(n+1)
        else:
            dnum1 = get_num_divisors(n)
            dnum2 = get_num_divisors((n+1)//2)
        dnum = dnum1 * dnum2
    return n*(n+1)//2

print(get_high_divisible_Tn(500))