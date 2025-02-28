from solutions.p031 import sum_coin_combinations


def test_sum_coin_combinations() -> None:
    assert sum_coin_combinations(200, [1, 2, 5, 10, 20, 50, 100, 200]) == 73682
