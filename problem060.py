import random

def is_maybe_prime(n, k=7):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

def check_list(plist):
    for p in plist:
        for q in plist:
            if p == q:
                continue
            if not is_maybe_prime(int(str(p)+str(q))):
                return False
    return True

def get_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10**4)

def get_prime_pairs():
    pairs = {}
    for i, p in enumerate(PRIMES):
        for q in PRIMES[i+1:]:
            if not is_pair(p, q):
                continue
            elif p in pairs:
                pairs[p].add(q)
            else:
                pairs[p] = {q}
    return pairs

def is_pair(p, q):
    num1 = int(str(p)+str(q))
    num2 = int(str(q)+str(p))
    if not is_maybe_prime(num1):
        return False
    elif not is_maybe_prime(num2):
        return False
    else:
        return True

def get_prime_triples(pairs):
    triples = {}
    for p, qvals in pairs.items():
        for q in qvals:
            if q not in pairs:
                continue
            for r in pairs[q]:
                if is_pair(p, r):
                    if p not in triples:
                        triples[p] = {}
                    
                    if q not in triples[p]:
                        triples[p][q] = {r}
                    else:
                        triples[p][q].add(r)
    return triples

def get_prime_quads(pairs, triples):
    quads = {}
    for p, pair in triples.items():
        for q, rvals in pair.items():
            for r in rvals:
                if r not in pair:
                    continue
                for s in pairs[r]:
                    if is_pair(p, s) and is_pair(q, s):
                        if p not in quads:
                            quads[p] = {}
                        if q not in quads[p]:
                            quads[p][q] = {}
                        
                        if r not in quads[p][q]:
                            quads[p][q][r] = {s}
                        else:
                            quads[p][q][r].add(s)
    return quads

def get_prime_quins(pairs, quads):
    quins = set()
    for p, triple in quads.items():
        for q, pair in triple.items():
            for r, svals in pair.items():
                for s in svals:
                    if s not in pair:
                        continue
                    for t in pairs[s]:
                        if is_pair(p, t) and is_pair(q, t) and is_pair(r, t):
                            quins.add((p, q, r, s, t))
    return quins

def get_smallest_prime_quins_sum():
    pairs = get_prime_pairs()
    triples = get_prime_triples(pairs)
    quads = get_prime_quads(pairs, triples)
    quins = get_prime_quins(pairs, quads)
    return min(sum(plist) for plist in quins)

print(get_smallest_prime_quins_sum())