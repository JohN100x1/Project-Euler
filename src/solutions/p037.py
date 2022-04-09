from utils.primes import get_primes


def sum_truncatable_primes(max_count=11) -> int:
    """Get the sum of all primes that are both left and right truncatable."""
    # Exclude first 4 primes from sum
    prime_sum = 0
    count = 0
    primes = get_primes(10**6)
    prime_set = set(primes)
    for p in primes[4:]:
        len_p = len(str(p))

        # Check Right truncatable
        if any(p // 10**i not in prime_set for i in range(len_p)):
            continue

        # Check left truncatable
        if any(p % pow(10, j) not in prime_set for j in range(len_p, 0, -1)):
            continue

        # Add prime to sum
        prime_sum += p
        count += 1

        # Since there are only 11, no further search is needed
        if count == max_count:
            break
    return prime_sum
