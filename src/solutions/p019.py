from datetime import datetime


def get_sunday_count(start_date: datetime, end_date: datetime) -> int:
    """Get the number of sunday starting months from start date to end date."""
    sundays = 0
    for year in range(start_date.year, end_date.year + 1):
        for month in range(start_date.month, end_date.month + 1):
            if datetime(year, month, 1).weekday() == 6:
                sundays += 1
    return sundays
