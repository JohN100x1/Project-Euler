from solutions.p016 import sum_digit


def test_sum_digit():
    assert sum_digit(2**1000) == 1366
