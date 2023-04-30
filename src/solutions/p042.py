from requests import get


def load_words() -> list[str]:
    """Load a list of words from p042_words.txt."""
    url = "https://projecteuler.net/project/resources/p042_words.txt"
    content = get(url).content.decode("utf-8")
    return content.replace('"', "").split(",")


def count_triangle_words(words: list[str]) -> int:
    """
    Get number of words which have a converted sum equal to a triangle number.
    """
    count = 0
    for word in words:
        t = sum(ord(L) - 64 for L in word)
        n = (-1 + (1 + 8 * t) ** 0.5) / 2
        if int(n) == n:
            count += 1
    return count
