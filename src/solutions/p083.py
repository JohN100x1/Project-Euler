import numpy as np

from config import path_res


def load_matrix() -> np.array:
    """Load the matrix of integers from /res/p081_matrix.txt"""
    path_txt = path_res / "p081_matrix.txt"
    return np.loadtxt(path_txt, dtype=np.int32, delimiter=",")


def get_adj(
    m: int, n: int, visited: dict[tuple[int, int], int], w: tuple[int, int]
) -> set[tuple[int, int]]:
    """Get a set of adjacent nodes to visit."""
    adj_nodes = set()
    north = (w[0] - 1, w[1])
    south = (w[0] + 1, w[1])
    west = (w[0], w[1] - 1)
    east = (w[0], w[1] + 1)
    if 0 < w[0] and north not in visited:
        adj_nodes.add(north)
    if w[0] < m - 1 and south not in visited:
        adj_nodes.add(south)
    if 0 < w[1] and west not in visited:
        adj_nodes.add(west)
    if w[1] < n - 1 and east not in visited:
        adj_nodes.add(east)
    return adj_nodes


def dijkstra(
    matrix: np.array, start: tuple[int, int], end: tuple[int, int]
) -> int:
    """Dijkstra's algorithm to find the minimal path."""
    m, n = matrix.shape
    path_sums1 = {start: matrix[start]}
    path_sums2 = {}
    while end not in path_sums2:
        w = min(path_sums1, key=path_sums1.get)
        path_sums2[w] = path_sums1.get(w)
        del path_sums1[w]
        for x in get_adj(m, n, path_sums2, w):
            if x not in path_sums1:
                path_sums1[x] = path_sums2[w] + matrix[x]
            elif path_sums2[w] + matrix[x] < path_sums1[x]:
                path_sums1[x] = path_sums2[w] + matrix[x]
    return path_sums2[end]


def get_four_way_min_path_sum(matrix: np.array) -> int:
    """Get the minimum path sum going starting top-left."""
    source = (0, 0)
    destination = (matrix.shape[0] - 1, matrix.shape[1] - 1)
    return dijkstra(matrix, source, destination)
