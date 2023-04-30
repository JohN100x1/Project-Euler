from solutions.p081 import load_matrix
from solutions.p083 import get_four_way_min_path_sum


def test_get_four_way_min_path_sum():
    matrix = load_matrix()
    assert get_four_way_min_path_sum(matrix) == 425185
