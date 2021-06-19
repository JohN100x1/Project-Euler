def self_pow(digits):
    S = 0
    for i in range(1, 1000):
        S += pow(i, i, 10**digits)
    return S % 10**digits

print(self_pow(10))