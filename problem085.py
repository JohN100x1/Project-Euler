def get_area_nearest_solution(C0, maxiters=1000):
    # Asserts that C0 is not a solution
    dC = 1
    Cvals = [C0 + dC, C0 - dC]
    for _ in range(maxiters):
        for C in Cvals:
            q = 16*C
            for x in range(2, int(1+(1+8*C**0.5)**0.5)//2+1):
                xxm1 = x*(x-1)
                if q % xxm1 != 0:
                    continue
                y = 0.5*(1+(1 + q//xxm1)**0.5)
                if int(y) == y:
                    A = (x-1)*(int(y)-1)
                    return A
        Cvals[0] += dC
        Cvals[1] -= dC

print(get_area_nearest_solution(2000000))