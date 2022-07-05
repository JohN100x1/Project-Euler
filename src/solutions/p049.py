from utils.exceptions import SolutionNotFoundError
from utils.primes import get_primes


def get_arth_prime_perms() -> int:
    """
    Get the number formed by concatenating 3 four-digit primes that are
    permutations of each other and form an arithmetic sequence.
    """

    primes = [p for p in get_primes(10000) if p > 999 and "0" not in str(p)]

    checked = {1487}
    for i, p in enumerate(primes):
        # Skipped checked primes
        if p in checked:
            continue
        checked.add(p)

        # Get prime permutations
        perms = []
        for p2 in primes[i + 1 :]:
            # Check if it is a permutation
            if sorted(str(p)) == sorted(str(p2)):
                perms.append(p2)

        # Check if primes form an arithmetic sequence
        for p3 in perms:
            d = p3 - p
            if p + 2 * d in perms:
                return int(str(p) + str(p3) + str(p + 2 * d))
    raise SolutionNotFoundError("Failed to solve p049.")
