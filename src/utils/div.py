def get_proper_factor_sums(n: int) -> list[int]:
    """Get a list of proper factor sums for all numbers less than n."""
    # Get the proper factor sums
    proper_factor_sums = [1] * n
    for i in range(2, int(n**0.5)):
        proper_factor_sums[i * i] += i
        for k in range(i + 1, n // i):
            proper_factor_sums[i * k] += i + k
    return proper_factor_sums
