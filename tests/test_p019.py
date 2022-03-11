from datetime import datetime

from solutions.p019 import get_sunday_count


def test_get_sunday_count():
    start_date = datetime(1901, 1, 1)
    end_date = datetime(2000, 12, 31)
    assert get_sunday_count(start_date, end_date) == 171
