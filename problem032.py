def is_pandigital_mmp(multiplicand, multiplier, product):
    # Assumes unique digits within multiplicand, multiplier, etc.
    multiplicand = set(int(x) for x in str(multiplicand))
    multiplier = set(int(x) for x in str(multiplier))
    product = set(int(x) for x in str(product))
    is_pandigital = True
    # Check contains all digits
    if multiplicand | multiplier | product != set(range(1,10)):
        is_pandigital = False
    # Check contains digit once
    A = len(multiplicand & multiplier) > 0
    B = len(multiplicand & product) > 0
    C = len(multiplier & product) > 0
    if A or B or C:
        is_pandigital = False
    return is_pandigital

def find_pandigital_mmp_sum():
    pandigitals = {}
    pandigital_mmp_sum = 0
    # Case with 1 digit number times 4 digit number
    for a in range(1,10):
        multiplicand = a
        for b in (set(range(1,10)) - {a}):
            for c in (set(range(1,10)) - {a,b}):
                for d in (set(range(1,10)) - {a,b,c}):
                    for e in (set(range(1,10)) - {a,b,c,d}):
                        multiplier = 1000*b+100*c+10*d+e
                        product = multiplicand*multiplier
                        if len(set(str(product))) != len(str(product)):
                            continue
                        if is_pandigital_mmp(multiplicand, multiplier, product):
                            pandigitals[product] = {multiplicand,multiplier}
                            pandigital_mmp_sum += product
    # Case with 2 digit number times 3 digit number
    for a in range(1,10):
        for b in (set(range(1,10)) - {a}):
            multiplicand = 10*a+b
            for c in (set(range(1,10)) - {a,b}):
                for d in (set(range(1,10)) - {a,b,c}):
                    for e in (set(range(1,10)) - {a,b,c,d}):
                        multiplier = 100*c+10*d+e
                        product = multiplicand*multiplier
                        if len(set(str(product))) != len(str(product)):
                            continue
                        if is_pandigital_mmp(multiplicand, multiplier, product):
                            pandigitals[product] = {multiplicand,multiplier}
                            pandigital_mmp_sum += product
    return sum(pandigitals.keys())

print(find_pandigital_mmp_sum())