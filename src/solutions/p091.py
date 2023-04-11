from math import gcd


def count_right_triangles(n: int) -> int:
    """
    Count the number of right triangles with integer vertices. 0 <= x, y <= n.
    """
    count = 0
    for x in range(n + 1):
        for y in range(n + 1):
            if x == 0 and y == 0:
                continue
            d = gcd(x, y)
            x_reduced, y_reduced = x // d, y // d
            if y_reduced != 0:
                down_count = (n - x) // y_reduced
            else:
                down_count = 100
            if x_reduced != 0:
                right_count = y // x_reduced
            else:
                count += down_count
                continue
            if down_count > right_count:
                count += right_count
            else:
                count += down_count
    return 2 * count + n * n
