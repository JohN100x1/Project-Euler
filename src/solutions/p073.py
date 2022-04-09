def total_frac(max_d: int) -> int:
    """Get the total number of fractions between 1/3 and 1/2."""
    q = max_d // 6
    r = max_d % 6
    f = q * (3 * q - 2 + r)
    if r == 5:
        f += 1
    return f


class SubLinearAlgorithm:
    """
    Use the sublinear algorithm to count the proper fractions.
    https://projecteuler.net/overview=073
    """

    def __init__(self, max_d: int):
        self.max_d = max_d
        self.k = int((max_d / 2) ** 0.5)
        self.m = int(max_d / (2 * self.k + 1))
        self.r_small = [0 for _ in range(self.m + 1)]
        self.r_large = [0 for _ in range(self.k)]

    def r_procedure(self, n: int):
        """Perform the R(n) procedure."""
        switch = int((n / 2) ** 0.5)
        count = total_frac(n) - total_frac(n // 2)
        m = 5
        k = (n - 5) // 10
        while k >= switch:
            next_k = (n // (m + 1) - 1) // 2
            count -= (k - next_k) * self.r_small[m]
            k = next_k
            m += 1
        while k > 0:
            m = n // (2 * k + 1)
            if m <= self.m:
                count -= self.r_small[m]
            else:
                count -= self.r_large[((self.max_d // m) - 1) // 2]
            k -= 1
        if n <= self.m:
            self.r_small[n] = count
        else:
            self.r_large[((self.max_d // n) - 1) // 2] = count

    def count_frac(self) -> int:
        """
        Get the number of proper fractions between 1/3 and 1/2 in the ordered
        list of proper fractions n/d where 1 <= n < d <= max_d.
        """
        for n in range(5, self.m + 1):
            self.r_procedure(n)
        for j in range(self.k - 1, -1, -1):
            self.r_procedure(self.max_d // (2 * j + 1))
        return self.r_large[0]
