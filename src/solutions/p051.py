def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(1000000)
PRIME_SET = set(PRIMES)

def get_perms(L, r):
    if len(L) == 1 or len(L) == r:
        return [L]
    else:
        perms = []
        hashes = set()
        for i in range(len(L)):
            l = L[:i] + L[i+1:]
            for perm in get_perms(l, r):
                h = hash(tuple(perm))
                if h not in hashes:
                    hashes.add(h)
                    perms.append(perm)
        return perms

def get_8_prime_family():
    # For an 8 prime value family,
    # 3 digits must be the same
    # Last digit cannot be changed
    
    # Get primes with a least 3 repeated digits
    # Get the repeated and remaining digit indexes
    # NOTE: since PRIMES < 10^6, there's only 1 rdigit
    repeated = {}
    for p in PRIMES:
        rdigit = None
        pstring = str(p)[::-1]
        dlists = {}
        for i, d in enumerate(map(int, pstring)):
            if d not in dlists:
                dlists[d] = [i]
            else:
                dlists[d].append(i)
                # Record indices of 3 digit repeats
                if len(dlists[d]) == 3:
                    rdigit = d
        if rdigit is not None:
            repeated[p] = dlists.pop(rdigit)
    # Pick 3 digit positions from repeated digits
    for p, idxs in repeated.items():
        for perm in get_perms(idxs, 3):
            family = {p}
            sub = sum(p % pow(10,i+1) - p %pow(10,i) for i in perm)
            base = p - sub
            increment = sum(1 * pow(10, i) for i in perm)
            for d in range(int(len(str(base)) < len(str(p))), 10):
                q = base + d*increment
                if q in PRIME_SET:
                    family.add(q)
            if len(family) == 8:
                return min(family)

print(get_8_prime_family())