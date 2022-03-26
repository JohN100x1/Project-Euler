from solutions.p011 import get_largest_prod, load_grid


def test_get_largest_prod():
    grid = load_grid()
    assert get_largest_prod(grid) == 70600674
