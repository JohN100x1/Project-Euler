from math import comb


def get_lattice_paths(n: int) -> int:
    """Get all lattice paths on a nxn grid."""
    return comb(2 * n, n)


if __name__ == "__main__":
    print(get_lattice_paths(20))
