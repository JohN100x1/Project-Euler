def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10000)

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

def get_amicable_sum(n):
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
    return amicable_sum

print(get_amicable_sum(10000))