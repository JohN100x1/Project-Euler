def get_num_divisors(n: int, primes: list) -> int:
    """Get the number of divisors of n."""
    if n == 1:
        return 1
    else:
        num_div = 1
        sqrtn = int(n**0.5) + 1
        for prime in primes:
            if prime < sqrtn:
                power = 1
                while n % prime == 0:
                    n //= prime
                    power += 1
                num_div *= power
            else:
                break
        return num_div
