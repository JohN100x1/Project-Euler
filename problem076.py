def get_partition_count(n0, n):
    if n == 1:
        return 0
    count = 0
    for n1, n2 in enumerate(range(n-1-n0,n//2-(1-n%2),-1),n0):
        count += 1 + get_partition_count(n1, n2)
    return count

print(get_partition_count(0, 100))