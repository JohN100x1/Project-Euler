import numpy as np

def get_primes(n):
    numbers = np.arange(n+1, dtype=np.int64)
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2,(n+1)//i+1):
                if j*i <= n:
                    is_prime[j*i] = False
        else:
            continue
    return numbers[is_prime]

PRIMES = get_primes(28123)

def get_prime_factorisation(n):
    if n <= 1:
        return {}
    x = 1*n
    products = {}
    for p in PRIMES:
        while x % p == 0:
            x //= p
            if p in products:
                products[p] += 1
            else:
                products[p] = 1
        if x == 1:
            break
    return products

def proper_factor_sum(n):
    if n <= 1:
        return 0
    factor_sum = 1
    prime_factors = get_prime_factorisation(n)
    primes = prime_factors.keys()
    for p in primes:
        m = prime_factors[p]
        factor_sum *= (p**(m+1)-1)/(p-1)
    factor_sum -= n
    return int(factor_sum)

def get_abundant_nums(n):
    abundant_nums = []
    for i in range(12,n+1):
        m = proper_factor_sum(i)
        if m > i:
            abundant_nums.append(i)
    return abundant_nums

ABUNDANTS = get_abundant_nums(28123)

def get_non_sum_two_abundant():
    # Get list of numbers (which are sum of two abundants)
    sta = set()
    for i, a in enumerate(ABUNDANTS):
        for b in ABUNDANTS[i:]:
            sta.add(a+b)
    # Get sum of numbers (which are NOT sum of two abundants)
    nsta_sum = sum(x for x in range(1,28123) if x not in sta)
    return nsta_sum

print(get_non_sum_two_abundant())