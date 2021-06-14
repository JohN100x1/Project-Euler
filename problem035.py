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

PRIMES = get_primes(1000000)

def count_circ_primes():
    prev_p = 0
    circ_primes = {2,3,5,7}
    for p in PRIMES:
        # Skip existing circular primes
        if p in circ_primes:
            continue
        dlist = [int(d) for d in str(p)]
        # Circular primes with >2 digits don't have these digits
        if len(set(dlist) & {2,4,5,6,8,0}) > 0:
            continue
        cyc_nums = set()
        # Roll the digits and check if they're prime (prime must have >2 digits)
        for j in range(len(str(p))):
            n = int("".join(str(x) for x in np.roll(dlist,j)))
            cyc_nums.add(n)
            if n not in PRIMES:
                break
        else:
            circ_primes = circ_primes | cyc_nums
    return len(circ_primes)

print(count_circ_primes())