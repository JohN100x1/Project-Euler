def count_distinct_powers(n: int) -> int:
    """Get the number of distinct a^b where a, b <= n."""
    distinct_powers = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            distinct_powers.add(a**b)
    return len(distinct_powers)


print(count_distinct_powers(100))
