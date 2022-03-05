def get_sunday_count(start_year: int, end_year: int) -> int:
    """Get the number of sundays from star year to end year."""
    non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    sundays = 0
    for year in range(start_year, end_year + 1):
        if start_year % 4 == 0:
            months = non_leap
        else:
            months = leap_year
        for month in months:
            days += month
            if days % 7 == 0:
                sundays += 1
    return sundays
