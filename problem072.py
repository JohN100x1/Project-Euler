def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def get_totient_sum(n):
    primes = get_primes(n)
    totients = [i for i in range(2,n+1)]
    for p in primes:
        totients[p-2::p] = [k-k//p for k in totients[p-2::p]]
    return sum(totients)

print(get_totient_sum(10**6))