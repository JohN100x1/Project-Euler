def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(28123)

def get_prime_factorisation(n):
    if n <= 1:
        return {}
    x = n
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
    for p, exp in prime_factors.items():
        factor_sum *= (p**(exp+1)-1)//(p-1)
    factor_sum -= n
    return factor_sum

def get_abundant_nums(n):
    abundant_nums = []
    for i in range(12,n+1):
        m = proper_factor_sum(i)
        if m > i:
            abundant_nums.append(i)
    return abundant_nums

def get_non_sum_two_abundant():
    abundants = get_abundant_nums(28123)
    # Get list of numbers (which are sum of two abundants)
    sta = set()
    for i, a in enumerate(abundants):
        for b in abundants[i:]:
            sta.add(a+b)
    # Get sum of numbers (which are NOT sum of two abundants)
    nsta_sum = sum(x for x in range(1,28123) if x not in sta)
    return nsta_sum

print(get_non_sum_two_abundant())