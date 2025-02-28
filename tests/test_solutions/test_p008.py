from solutions.p008 import get_largest_product, load_str_digits


def test_get_largest_product() -> None:
    str_digits = load_str_digits()
    assert get_largest_product(13, str_digits) == 23514624000
