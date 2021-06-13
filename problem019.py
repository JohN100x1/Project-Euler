non_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]

def count_sundays(x, y):
    days = 0
    sundays = 0
    for year in range(x, y+1):
        if x % 4 == 0:
            months = leap_year
        else:
            months = non_leap
        for month in months:
            days += month
            if days % 7 == 0:
                sundays += 1
    return sundays

print(count_sundays(1901,2000))