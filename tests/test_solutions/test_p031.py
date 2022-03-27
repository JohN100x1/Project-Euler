from solutions.p031 import count_coin_sum_comb


def test_count_coin_sum_comb():
    assert count_coin_sum_comb([1, 2, 5, 10, 20, 50, 100, 200], 200) == 73682
