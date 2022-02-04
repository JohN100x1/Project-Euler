def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def get_min_totient_ratio_perm(n):
    ratios = {}
    primes = get_primes(n)
    totients = [i for i in range(2,n)]
    for p in primes:
        totients[p-2::p] = [k-k//p for k in totients[p-2::p]]
    for i, t in enumerate(totients, 2):
        if sorted(str(i)) == sorted(str(t)):
            ratios[i] = i/t
    return min(ratios, key=ratios.get)

print(get_min_totient_ratio_perm(10**7))