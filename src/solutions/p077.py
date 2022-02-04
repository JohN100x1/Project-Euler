def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10**2)
PRIME_SET = set(PRIMES)

def get_prime_partition_count(n0, n):
    if n in {2, 3}:
        return 0
    count = 0
    for n1 in (p for p in PRIMES if n0 <= p and p <= n//2):
        n2 = n - n1
        if n2 in PRIME_SET:
            count += 1 + get_prime_partition_count(n1, n2)
        else:
            count += get_prime_partition_count(n1, n2)
    return count

def get_prime_partition_num_over(N):
    n = 4
    while get_prime_partition_count(2, n) < N:
        n += 1
    return n

print(get_prime_partition_num_over(5000))