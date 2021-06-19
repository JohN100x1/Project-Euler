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
PRIMES = PRIMES[PRIMES > 999]
PRIMES = [p for p in PRIMES if "0" not in str(p)]

def find_arth_prime_perms():
    checked = {1487}
    concatenated = ""
    for i, p in enumerate(PRIMES):
        # Skipped checked primes
        if p in checked:
            continue
        else:
            checked.add(p)
        # Get prime permutations
        perms = []
        for p2 in PRIMES[i+1:]:
            # Check if it is a permutation
            if sorted(str(p)) == sorted(str(p2)):
                perms.append(p2)
        # Check if primes form an arthmetic sequence
        for p3 in perms:
            d = p3 - p
            if p + 2*d in perms:
                concatenated = str(p) + str(p3) + str(p + 2*d)
                break
        if concatenated != "":
            break
    return int(concatenated)

print(find_arth_prime_perms())