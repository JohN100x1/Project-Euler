def count_partitions(n: int) -> int:
    """Get the number of partitions n can be split into."""
    plist = [1, 1]
    for x in range(2, n + 1):
        partition_sum = 0
        sqrt1p24x = (1 + 24 * x) ** 0.5
        for k in range(1, int(1 + sqrt1p24x) // 6 + 1):
            partition_sum += (-1) ** (k + 1) * plist[x - k * (3 * k - 1) // 2]
        for k in range(1, int(-1 + sqrt1p24x) // 6 + 1):
            partition_sum += (-1) ** (k + 1) * plist[x - k * (3 * k + 1) // 2]
        plist.append(partition_sum)
    return plist[n] - 1
