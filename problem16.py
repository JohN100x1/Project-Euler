def get_digit_sum(x):
    digit_sum = sum(int(i) for i in str(x))
    return digit_sum

print(get_digit_sum(2**1000))