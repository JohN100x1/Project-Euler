def get_area_nearest_solution(start_count: int, limit=1000) -> int:
    """
    Get the area of the rectangle such that the number of sub-rectangles is
    closest to 2 million.

    No rectangle has 2 million sub-rectangles.
    """
    counts = [start_count + 1, start_count - 1]
    for _ in range(limit):
        for count in counts:
            q = 16 * count
            for x in range(2, int(1 + (1 + 8 * count**0.5) ** 0.5) // 2 + 1):
                xxm1 = x * (x - 1)
                if q % xxm1 != 0:
                    continue
                y = 0.5 * (1 + (1 + q // xxm1) ** 0.5)
                if int(y) == y:
                    return (x - 1) * (int(y) - 1)
        counts[0] += 1
        counts[1] -= 1
