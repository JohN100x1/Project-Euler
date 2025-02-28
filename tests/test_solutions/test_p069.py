from solutions.p069 import get_max_ratio


def test_get_max_ratio() -> None:
    assert get_max_ratio(10**6) == 510510
