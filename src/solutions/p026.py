def get_cycle_len(d):
    cycle_len = 0
    # Dict {div : [remainder, idx]}
    div_remainder = {}
    # Long division 1/d
    decimal = [1] + [0]*1000
    for i in range(len(decimal)-1):
        x = decimal[i]
        div = x//d
        remainder = x % d
        decimal[i] = div
        decimal[i+1] += 10*remainder
        if div in div_remainder:
            if div_remainder[div][0] == remainder:
                cycle_len = i - div_remainder[div][1]
                break
        else:
            div_remainder[div] = [remainder, i]
    return cycle_len

def get_max_cycle(n):
    max_d = 1
    max_cycle_len = 0
    for d in range(2,n):
        cycle_len = get_cycle_len(d)
        if cycle_len > max_cycle_len:
            max_d = d
            max_cycle_len = cycle_len
    return max_d

print(get_max_cycle(1000))