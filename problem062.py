def get_digit_tuple(n):
    y = n
    dlist = [0] * 10
    while y != 0:
        d = y % 10
        dlist[d] += 1
        y //= 10
    return tuple(dlist)

def get_smallest_cube_with_5_perm():
    tups = {}
    for n in range(10000):
        cube = n**3
        tup = get_digit_tuple(cube)
        if tup not in tups:
            tups[tup] = {cube}
        else:
            tups[tup].add(cube)
            if len(tups[tup]) == 5:
                return min(tups[tup])
            
print(get_smallest_cube_with_5_perm())