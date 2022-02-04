NON_LEAP = [31,28,31,30,31,30,31,31,30,31,30,31]
LEAP_YEAR = [31,29,31,30,31,30,31,31,30,31,30,31]

def get_sunday_count(x, y):
    days = 0
    sundays = 0
    for year in range(x, y+1):
        if x % 4 == 0:
            months = NON_LEAP
        else:
            months = LEAP_YEAR
        for month in months:
            days += month
            if days % 7 == 0:
                sundays += 1
    return sundays

print(get_sunday_count(1901,2000))