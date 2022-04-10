def get_primes(n: int) -> list:
    """Returns a list of primes less than n."""
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def is_composite(a: int, d: int, n: int, s: int) -> bool:
    """Check if n is a composite using Miller-Rabin."""
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True


def miller_rabin_is_prime(n: int) -> bool:
    """Primality test using Miller-Rabin test with witnesses."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(is_composite(a, d, n, s) for a in (2, 3))
    elif n < 25326001:
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5))
    elif n < 118670087467:
        if n == 3215031751:
            return False
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5, 7))
    else:
        raise ValueError("n is too large.")
