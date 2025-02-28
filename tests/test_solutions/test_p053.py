from solutions.p053 import count_ncr_greater_than


def test_count_ncr_greater_than() -> None:
    assert count_ncr_greater_than(10**6) == 4075
