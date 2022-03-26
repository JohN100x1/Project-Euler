from math import comb


def count_lattice_paths(n: int) -> int:
    """Get the number of lattice paths on a nxn grid."""
    return comb(2 * n, n)
