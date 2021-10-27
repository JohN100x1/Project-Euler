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

def search_n_len_prime_family(n, max_digits=6):
    digits = 0
    while digits < max_digits:
        digits += 1
        lbound = 10**(digits-1)
        ubound = 10**digits
        primes = PRIMES[PRIMES <= ubound]
        primes = primes[primes >= lbound]
        dlists = get_dlist_combinations(digits)[1:]
        npv_families = []
        for dlist in dlists:
            prime_families = get_prime_digit_families(primes, dlist)
            for family in prime_families.values():
                if len(family) == n:
                    npv_families.append(family)
        if len(npv_families) > 0:
            return min(min(family) for family in npv_families)
    return None

def get_dlist_combinations(size):
    nums = list(range(size))
    dlists = []
    for mask in range(1<<size):
        dlist = []
        for pos in range(size):
            if (mask & (1<<pos)):
                dlist.append(nums[pos])
        dlists.append(dlist)
    return dlists

def get_prime_digit_families(primes, dlist):
    checked = set()
    prime_families = {}
    for p in primes:
        if p not in checked:
            checked.add(p)
            p_string = get_p_string(p, dlist)
            if p_string == "INVALID":
                pass
            elif p_string in prime_families:
                prime_families[p_string].add(p)
            else:
                prime_families[p_string] = {p}
    return prime_families

def get_p_string(p, dlist):
    s = ""
    p = str(p)
    match = set()
    for i in range(len(p)):
        if i in dlist:
            s += p[i]
        else:
            if p[i] not in match:
                match.add(p[i])
            s += "*"
    if len(match) > 1:
        return "INVALID"
    return s

print(search_n_len_prime_family(8))