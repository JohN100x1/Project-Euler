def get_most_sol_pytriple(N):
    # https://www.desmos.com/calculator/atmk2vllqr
    pmax = 0
    max_sols = 0
    for p in range(2, N+1):
        sols = 0
        for x in range(1, int(p*(1-0.5*2**0.5))+1):
            if p*(p-2*x) % (2*(p-x)) == 0:
                sols += 1
        if sols > max_sols:
            pmax = p
            max_sols = sols
    return pmax

print(get_most_sol_pytriple(1000))