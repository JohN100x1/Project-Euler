from solutions.p066 import get_max_diophantine


def test_get_max_diophantine() -> None:
    assert get_max_diophantine(1000) == 661
