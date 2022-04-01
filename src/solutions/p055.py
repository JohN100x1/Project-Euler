def count_lychrel_nums(n: int) -> int:
    """Get the number of Lychrel numbers below n < 10,000."""
    count = 0
    for x in range(1, n):
        for iterations in range(50):
            x += int(str(x)[::-1])
            if str(x) == str(x)[::-1]:
                break
        else:
            count += 1
    return count
