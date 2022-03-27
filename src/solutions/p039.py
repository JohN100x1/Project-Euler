def get_perimeter_most_pytriple_sol(n: int) -> int:
    """
    Get the value of p <= n such that a + b + c = p and a^2 + b^2 = c^2
    has the most pythagorean triples.

    https://www.desmos.com/calculator/atmk2vllqr
    """
    max_p = 0
    max_sols = 0
    for p in range(2, n + 1):
        sols = 0
        for x in range(1, int(p * (1 - 0.5 * 2**0.5)) + 1):
            if p * (p - 2 * x) % (2 * (p - x)) == 0:
                sols += 1
        if sols > max_sols:
            max_p = p
            max_sols = sols
    return max_p
