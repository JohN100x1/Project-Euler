from math import factorial

def factorial_digit_sum(n):
    digit_sum = sum(int(d) for d in str(factorial(n)))
    return digit_sum

print(factorial_digit_sum(100))