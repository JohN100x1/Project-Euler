from solutions.p089 import count_numerals_saved, load_numerals


def test_count_numerals_saved() -> None:
    numerals = load_numerals()
    assert count_numerals_saved(numerals) == 743
