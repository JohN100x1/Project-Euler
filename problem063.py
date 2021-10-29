def get_nth_digit_power_count():
    count = 0
    n = 1
    lbound = pow(10,1-1/n)
    while lbound <= 9:
        count += 10+int(-lbound//1)
        n += 1
        lbound = pow(10,1-1/n)
    return count

print(get_nth_digit_power_count())