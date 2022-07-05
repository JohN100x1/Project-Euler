from utils.exceptions import SolutionNotFoundError


def get_first_consecutive_distinct_prime_factors(max_n: int = 200000) -> int:
    """
    Get the first of 4 consecutive numbers such that they have distinct
    prime factors.
    """
    counter = 0
    num_factors = [0 for _ in range(max_n)]
    for n in range(2, max_n):
        # Prime number
        if num_factors[n] == 0:
            counter = 0
            for multiple in range(max_n // n):
                num_factors[n * multiple] += 1
        # Composite with 4 Distinct factors
        elif num_factors[n] == 4:
            counter += 1
            if counter == 4:
                return n - 3
        # Composite with Distinct factors != 4
        else:
            counter = 0
    raise SolutionNotFoundError("Failed to solve p047.")
