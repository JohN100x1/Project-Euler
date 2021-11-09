FACTORIAL = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def get_sum_digit_factorial(n):
    dfsum = FACTORIAL[n % 10]
    while n // 10 != 0:
        n //= 10
        dfsum += FACTORIAL[n%10]
    return dfsum