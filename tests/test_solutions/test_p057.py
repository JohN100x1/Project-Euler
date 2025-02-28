from solutions.p057 import count_sqrt2_continued_fraction_numer_digit


def test_get_sqrt2_continued_fraction_digit_count() -> None:
    assert count_sqrt2_continued_fraction_numer_digit(1000) == 153
