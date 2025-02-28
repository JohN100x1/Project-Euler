from solutions.p022 import load_names, sum_name_scores


def test_sum_name_scores() -> None:
    names = load_names()
    assert sum_name_scores(names) == 871198282
