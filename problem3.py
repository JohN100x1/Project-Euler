def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_largest_prime_factor(n: int) -> int:
    f = n
    sqrtn = int(n**0.5) + 1
    if sqrtn % 2 == 0:
        sqrtn -= 1
    for j in range(sqrtn,1,-2):
        if n % j == 0 and is_prime(j):
            f = j
            break
    if f == n and n % 2 == 0:
        f = 2
    return f

print(find_largest_prime_factor(600851475143))