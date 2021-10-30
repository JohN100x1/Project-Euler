def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10000)
PRIME_SET = set(PRIMES)

def get_quadratic_primes_longest_pair_product(N):
    qp_pairs = {}
    for a in range(-1000,1000):
        for b in [p for p in PRIMES if p < 1000]:
            for n in range(1,N+1):
                if n**2 + a*n + b not in PRIME_SET:
                    qp_pairs[(a,b)] = n-1
                    break
            else:
                qp_pairs[(a,b)] = n
    max_pair = max(qp_pairs, key=qp_pairs.get)
    product = max_pair[0] * max_pair[1]
    return product

print(get_quadratic_primes_longest_pair_product(100))