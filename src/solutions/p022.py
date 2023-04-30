from requests import get


def load_names() -> list[str]:
    """Load a list of names from p022_names.txt."""
    url = "https://projecteuler.net/project/resources/p022_names.txt"
    content = get(url).content.decode("utf-8")
    return content.replace('"', "").split(",")


def name_score(pos: int, name: str) -> int:
    """Calculate name score for a given name and position."""
    score = pos * sum(ord(letter) - 64 for letter in name)
    return score


def sum_name_scores(names: list[str]) -> int:
    """Get the sum of the names scores of a list of names."""
    total_score = 0
    sorted_names = sorted(names)
    for pos, name in enumerate(sorted_names, 1):
        total_score += name_score(pos, name)
    return total_score
