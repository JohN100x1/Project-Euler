def find_4_consecutive_distinct_prime_factors(N):
    answer = None
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
                answer = n - 3
                break
        # Composite with Distinct factors != 4
        else:
            counter = 0
    return answer

print(find_4_consecutive_distinct_prime_factors(200000))