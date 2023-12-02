from re import findall

from requests import get


def load_paths() -> list[list[int]]:
    """Load a binomial tree path as a list of lists."""
    url = "https://projecteuler.net/problem=18"
    content = get(url).content.decode("utf-8")
    first_num = r'<p class="monospace center">(\d+)<br>'
    pattern = r"\n([\d ]+)(?:<br>|</p>)"
    lines = findall(first_num, content)
    lines.extend(findall(pattern, content))
    paths = [[int(n) for n in line.split(" ")] for line in lines]
    return paths


def get_max_path(paths: list[list[int]]) -> int:
    """Get the maximum path of a binomial tree."""
    for i in range(len(paths) - 2, -1, -1):
        for j in range(len(paths[i])):
            paths[i][j] += max(paths[i + 1][j], paths[i + 1][j + 1])
    return paths[0][0]
