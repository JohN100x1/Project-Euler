from typing import Generator


def generate_point(n: int) -> Generator[tuple[int, int], None, None]:
    """Generate integer points (x, y) != (0, 0) and 0 <= x, y <= n."""
    for y in range(1, n + 1):
        yield 0, y
    for x in range(1, n + 1):
        for y in range(n + 1):
            yield x, y


def count_right_triangles(n: int) -> int:
    """
    Count the number of right triangles with integer vertices. 0 <= x, y <= n.
    """
    count = 0
    for px, py in generate_point(n):
        for qx, qy in generate_point(n):
            if px == qx and py == qy:
                continue
            if qy - py >= qx - px:
                continue
            pqx = qx - px
            pqy = qy - py
            if px * qx + py * qy == 0:
                count += 1
            elif px * pqx + py * pqy == 0:
                count += 1
            elif qx * pqx + qy * pqy == 0:
                count += 1
            else:
                continue
    return count
