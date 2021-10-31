def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = get_primes(10000)
PRIMES = [p for p in PRIMES if p > 999]
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