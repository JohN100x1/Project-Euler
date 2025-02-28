def count_unique_pytriple_with_perimeter(max_p: int) -> int:
    """
    Get the number of pythagorean triples with 1 solution for a particular
    perimeter, up to a perimeter of max_p.
    """
    perimeters = [sum(triple) for triple in get_triples(max_p)]
    solutions = {}
    for p in perimeters:
        for i in range(p, max_p + 1, p):
            solutions[i] = 0 if i in solutions else 1
    return sum(solutions.values())


def get_triples(
    max_p: int, a: int = 3, b: int = 4, c: int = 5
) -> list[tuple[int, int, int]]:
    """
    Get a list of 3-tuples which are Pythagorean triples with a max
    perimeter of max_p.
    """
    if a + b + c > max_p:
        return []
    triples = [(a, b, c)]
    a1, b1, c1 = a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c
    a2, b2, c2 = a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c
    a3, b3, c3 = -a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c
    triples += get_triples(max_p, a1, b1, c1)
    triples += get_triples(max_p, a2, b2, c2)
    triples += get_triples(max_p, a3, b3, c3)
    return triples
