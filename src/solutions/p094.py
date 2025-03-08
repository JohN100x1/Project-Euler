from math import gcd
from typing import Generator


def generate_py_triples(k: int) -> Generator[int, None, None]:
    """Generate Pythagorean triples."""
    for m in range(2, int(k**0.5) + 1):
        for n in range(m % 2 + 1, m, 2):
            c = m**2 + n**2
            if c > k:
                break
            if gcd(m, n) == 1:
                yield m**2 - n**2, 2 * m * n, c


def sum_almost_equilateral_perimeters(n: int) -> int:
    """
    Get the sum of all perimeters of all isosceles triangles with integral area
    and integer side lengths that differ no more than 1 with perimeter <= n
    The Almost equilateral triangles can be obtained by gluing two identical
    Pythagorean triples c-c-2a or c-c-2b
    """
    sum_perimeters = 0
    for a, b, c in generate_py_triples(n // 3 + 2):
        if abs(2 * a - c) == 1:
            sum_perimeters += 2 * a + 2 * c
        if abs(2 * b - c) == 1:
            sum_perimeters += 2 * b + 2 * c

    return sum_perimeters
