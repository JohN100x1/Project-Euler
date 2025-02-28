from solutions.p025 import get_nth_fibonacci_digits


def test_get_nth_fibonacci_digits() -> None:
    assert get_nth_fibonacci_digits(1000) == 4782
