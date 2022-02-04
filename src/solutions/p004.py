def get_largest_palindrome_product(n: int) -> int:
    """Gets the largest palindrome that is the product of 2 n-digit numbers."""
    ubound = 10**n - 1
    lbound = 10 ** (n - 1)
    palindrome = 0
    for i in range(ubound, lbound, -1):
        for j in range(ubound, i, -1):
            k = i * j
            if str(k) == str(k)[::-1] and k >= palindrome:
                palindrome = k
    return palindrome
