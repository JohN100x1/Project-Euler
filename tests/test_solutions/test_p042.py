from solutions.p042 import count_triangle_words, load_words


def test_count_triangle_words():
    words = load_words()
    assert count_triangle_words(words) == 162
