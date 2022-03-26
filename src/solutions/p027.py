from utils.primes import get_primes


def get_quadratic_primes_longest_pair_product() -> int:
    """
    Get the product of a and b such that m is maximised for the statement:
    n^2 + an + b is prime for all 0 <= n <= m, |a| < 1000, |b| <= 1000
    """

    primes = get_primes(100000)
    prime_set = set(primes)
    bounded_primes = [p for p in primes if p <= 1000]

    qp_pairs = {}
    for a in range(-999, 1000):
        for b in bounded_primes:
            n = 1
            while n**2 + a * n + b in prime_set:
                n += 1
            qp_pairs[(a, b)] = n - 1
    max_pair = max(qp_pairs, key=qp_pairs.get)
    product = max_pair[0] * max_pair[1]
    return product


print(get_quadratic_primes_longest_pair_product())
