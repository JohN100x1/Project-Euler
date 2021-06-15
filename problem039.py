def find_most_sol_pytriple(N):
    sols = {}
    for p in range(2, N+1):
        for x in range(1, int(p*(1-0.5*2**0.5))+1):
            y = p*(p-2*x)/(2*(p-x))
            if y == int(y):
                if p in sols.keys():
                    sols[p] += 1
                else:
                    sols[p] = 1
    return max(sols, key=sols.get)

print(find_most_sol_pytriple(1000))