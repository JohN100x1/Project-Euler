def get_polygonals(P):
    nums = {}
    n = 1
    Pn = P(n)
    while Pn < 10**4:
        half2 = Pn % 100
        if Pn >= 10**3 and half2 >= 10:
            half1 = (Pn-half2)//100
            if half1 not in nums:
                nums[half1] = {half2}
            else:
                nums[half1].add(half2)
        n += 1
        Pn = P(n)
    return nums

def get_cyclic_polygonals_sum():
    global cyclic_polys
    Plist = []
    Plist.append(get_polygonals(lambda n: n*(n+1)//2))
    Plist.append(get_polygonals(lambda n: n**2))
    Plist.append(get_polygonals(lambda n: n*(3*n-1)//2))
    Plist.append(get_polygonals(lambda n: n*(2*n-1)))
    Plist.append(get_polygonals(lambda n: n*(5*n-3)//2))
    Plist.append(get_polygonals(lambda n: n*(3*n-2)))
    
    cyclic_polys = []
    
    for i in range(len(Plist)):
        for v in Plist[i]:
            dfs_cylic_polygonals(Plist, [v], [i])
        if len(cyclic_polys) > 0:
            break
    
    tenssum = sum(tens for tens in cyclic_polys[0][:-1])
    hundsum = sum(hund for hund in cyclic_polys[0][1:])
    polysum = tenssum + 100*hundsum
    
    return polysum

def dfs_cylic_polygonals(Plist, chain, poly):
    global cyclic_polys
    depth = len(chain) - 1
    if depth == 5:
        if chain[0] in Plist[poly[-1]][chain[-1]]:
            cyclic_polys.append(chain + [chain[0]])
        return
    for i in range(len(Plist)):
        if i in poly:
            continue
        j = poly[-1]
        new_poly = poly + [i]
        for half2 in Plist[j][chain[-1]]:
            if half2 in Plist[i]:
                new_chain = chain + [half2]
                dfs_cylic_polygonals(Plist, new_chain, new_poly)
    return

print(get_cyclic_polygonals_sum())