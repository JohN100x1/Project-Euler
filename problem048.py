def get_self_pow_sum(digits):
    S = 0
    for i in range(1, 1000):
        S += pow(i, i, 10**digits)
    return S % 10**digits

print(get_self_pow_sum(10))