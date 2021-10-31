def get_sum_pandigitals(digits):
    # Only two possible ways for 1-9 pandigital is
    # 1 digit * 4 digit or 2 digit * 3 digit
    # Therefore the product must be 4 digits
    products = set()
    pfuncts = [
        lambda a, b, c, d, e: a*(1000*b+100*c+10*d+e),
        lambda a, b, c, d, e: (10*a+b)*(100*c+10*d+e)
        ]
    for a in digits:
        for b in (digits - {a}):
            for c in (digits - {a,b}):
                for d in (digits - {a,b,c}):
                    for e in (digits - {a,b,c,d}):
                        for pf in pfuncts:
                            product = pf(a, b, c, d, e)
                            if 1000 < product and product < 10000:
                                pset = set(map(int, str(product)))
                                if pset == digits - {a, b, c, d, e}:
                                    products.add(product)
    return sum(products)

print(get_sum_pandigitals({1,2,3,4,5,6,7,8,9}))