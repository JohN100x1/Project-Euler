from solutions.p081 import get_two_way_min_path_sum, load_matrix


def test_get_two_way_min_path_sum() -> None:
    matrix = load_matrix()
    assert get_two_way_min_path_sum(matrix) == 427337
