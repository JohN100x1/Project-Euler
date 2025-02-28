from solutions.p073 import SubLinearAlgorithm


def test_count_frac() -> None:
    assert SubLinearAlgorithm(12000).count_frac() == 7295372
