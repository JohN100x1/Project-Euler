from solutions.p046 import get_goldbach_counter_example


def test_get_goldbach_counter_example() -> None:
    assert get_goldbach_counter_example() == 5777
