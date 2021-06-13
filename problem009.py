def find_special_pytriple():
    abc = None
    for a in range(1,501):
        if (500000 - 1000*a) % (1000 - a) == 0:
            b = (500000 - 1000*a) // (1000 - a)
            abc = a*b*(1000 - a - b)
            break
    return abc

print(find_special_pytriple())