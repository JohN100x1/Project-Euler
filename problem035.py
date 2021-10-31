def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(1000000)
PRIME_SET = set(PRIMES)

def get_circ_prime_count():
    circ_primes = {2,3,5,7}
    nope_digits = {0,2,4,5,6,8}
    for p in PRIMES:
        # Skip existing circular primes
        if p in circ_primes:
            continue
        m = 0
        # Circular primes with >2 digits don't have these digits
        for d in map(int, str(p)):
            if d in nope_digits:
                break
            m += 1
        else:
            cyc_nums = set()
            # Roll the digits and check if they're prime
            for j in range(m):
                div = pow(10, j)
                n = (p % div)*pow(10, m-j) + p//div
                if n not in PRIME_SET:
                    break
                cyc_nums.add(n)
            else:
                circ_primes |= cyc_nums
    return len(circ_primes)

print(get_circ_prime_count())