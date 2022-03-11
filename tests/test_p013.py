from solutions.p013 import get_first_ten_digits, load_nums


def test_get_first_ten_digits():
    nums = load_nums()
    assert get_first_ten_digits(nums) == 5537376230
