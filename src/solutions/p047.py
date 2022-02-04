def get_4_consecutive_distinct_prime_factors(N=200000):
    counter = 0
    num_factors = [0 for i in range(N)]
    for n in range(2, N):
        # Prime number
        if num_factors[n] == 0:
            counter = 0
            for multiple in range(N//n):
                num_factors[n*multiple] += 1
        # Composite with 4 Distinct factors
        elif num_factors[n] == 4:
            counter += 1
            if counter == 4:
                return n - 3
        # Composite with Distinct factors != 4
        else:
            counter = 0
    return None

print(get_4_consecutive_distinct_prime_factors())