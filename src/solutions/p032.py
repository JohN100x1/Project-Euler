def sum_pandigital_products_one_to_nine() -> int:
    """
    Get the sum of all 1-9 pandigital multiplicand * multiplier = product

    Only two possible ways for 1-9 pandigital is
    1 digit * 4 digit or 2 digit * 3 digit, with a 4 digit product
    """

    def product14(u: int, v: int, x: int, y: int, z: int) -> int:
        return u * (1000 * v + 100 * x + 10 * y + z)

    def product23(u: int, v: int, x: int, y: int, z: int) -> int:
        return (10 * u + v) * (100 * x + 10 * y + z)

    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    products = set()
    product_functions = [product14, product23]
    for a in digits:
        for b in digits - {a}:
            for c in digits - {a, b}:
                for d in digits - {a, b, c}:
                    for e in digits - {a, b, c, d}:
                        for f in product_functions:
                            product = f(a, b, c, d, e)
                            if 1000 < product < 10000:
                                remaining_digits = set(map(int, str(product)))
                                leftover_digits = digits - {a, b, c, d, e}
                                if remaining_digits == leftover_digits:
                                    products.add(product)
    return sum(products)
