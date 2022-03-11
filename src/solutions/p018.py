from config import path_res


def load_paths() -> list[list[int]]:
    """Load a binomial tree path as a list of lists."""
    with open(path_res / "p018_numbers.txt", "r") as f:
        lines = f.read().split("\n")
        paths = [[int(n) for n in line.split(" ")] for line in lines]
    return paths


def get_max_path(paths: list[list[int]]) -> int:
    """Get the maximum path of a binomial tree."""
    for i in range(len(paths) - 2, -1, -1):
        for j in range(len(paths[i])):
            paths[i][j] += max(paths[i + 1][j], paths[i + 1][j + 1])
    return paths[0][0]
