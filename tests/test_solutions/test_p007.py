from solutions.p007 import get_nth_prime


def test_get_nth_prime() -> None:
    assert get_nth_prime(10001) == 104743
