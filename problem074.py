FACTORIAL = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def get_sum_digit_factorial(n):
    dfsum = FACTORIAL[n % 10]
    while n // 10 != 0:
        n //= 10
        dfsum += FACTORIAL[n%10]
    return dfsum

def get_count_with_chain_length(L, N):
    chain = {}
    count = 0
    for n0 in range(N):
        n = n0
        sublist = []
        subchain = {}
        subcount = 0
        while n not in chain and n not in subchain:
            subchain[n] = subcount
            sublist.append(n)
            subcount += 1
            n = get_sum_digit_factorial(n)
        if n in chain:
            for i, m in enumerate(reversed(sublist)):
                chain[m] = chain[n] + i + 1
        elif n in subchain:
            for i, m in enumerate(sublist):
                if i >= subchain[n]:
                    chain[m] = subcount - subchain[n]
                else:
                    chain[m] = len(sublist) - i
        if chain[n0] >= L:
            count += 1
    return count

print(get_count_with_chain_length(60,10**6))