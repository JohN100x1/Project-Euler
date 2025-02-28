from solutions.p064 import count_odd_sqrt_periods


def test_count_odd_sqrt_periods() -> None:
    assert count_odd_sqrt_periods(10000) == 1322
