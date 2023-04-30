from solutions.p081 import load_matrix
from solutions.p082 import get_three_way_min_path_sum


def test_get_three_way_min_path_sum():
    matrix = load_matrix()
    assert get_three_way_min_path_sum(matrix) == 260324
