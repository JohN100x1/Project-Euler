def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(1000000)
PRIME_SET = set(PRIMES)

def get_truncatable_prime_sum(max_count=11):
    # Exclude first 4 primes from sum
    psum = 0
    count = 0
    for p in PRIMES[4:]:
        plen = 1
        n = p
        # Check Right truncatable
        while n // 10 > 0:
            n //= 10
            plen += 1
            if n not in PRIME_SET:
                break
        else:
            # Check left truncatable
            for j in range(plen,0,-1):
                n = p % pow(10, j)
                if n not in PRIME_SET:
                    break
            else:
                psum += p
                count += 1
        # Since there are only 11, no further search is needed
        if count == max_count:
            break
    return psum

print(get_truncatable_prime_sum())