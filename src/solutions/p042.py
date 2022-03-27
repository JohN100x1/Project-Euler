from config import path_res


def load_words() -> list[str]:
    """Loads a list of strings from /res/p042_words.txt."""
    with open(path_res / "p042_words.txt") as f:
        return f.read().replace('"', "").split(",")


def count_triangle_words(words: list[str]) -> int:
    """
    Get the number of words which have a converted sum
    equal to a triangle number.
    """
    count = 0
    for word in words:
        t = sum(ord(L) - 64 for L in word)
        n = (-1 + (1 + 8 * t) ** 0.5) / 2
        if int(n) == n:
            count += 1
    return count
