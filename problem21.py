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

PRIMES = get_primes(10000)

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

def find_amicable_sum(n):
    checked = set()
    amicable_sum = 0
    for a in range(1,n):
        # Skip checked numbers
        if a in checked:
            continue
        # Check amicable
        b = proper_factor_sum(a)
        if proper_factor_sum(b) == a and a != b:
            amicable_sum += a + b
            checked.add(a)
            checked.add(b)
        else:
            checked.add(a)
            checked.add(b)
    return amicable_sum

print(find_amicable_sum(10000))