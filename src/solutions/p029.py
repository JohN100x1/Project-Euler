def get_distinct_powers_len(n):
    distinct_powers = set()
    for a in range(2, n+1):
        for b in range(2, n+1):
            distinct_powers.add(a**b)
    return len(distinct_powers)

print(get_distinct_powers_len(100))