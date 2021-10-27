def get_max_digit_sum(N):
    max_dsum = 0
    for a in range(1, N):
        for b in range(1, N):
            dsum = sum(int(d) for d in str(pow(a, b)))
            if dsum > max_dsum:
                max_dsum = dsum
    return max_dsum

print(get_max_digit_sum(100))