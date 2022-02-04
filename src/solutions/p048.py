def get_self_pow_sum(d):
    S = 0
    for i in range(1, 1000):
        S += pow(i, i, 10**d)
        S %= pow(10, d)
    return S

print(get_self_pow_sum(10))