from solutions.p094 import sum_almost_equilateral_perimeters


def test_sum_almost_equilateral_perimeters() -> None:
    assert sum_almost_equilateral_perimeters(1_000_000_000) == 518408346
