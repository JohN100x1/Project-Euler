def get_palindrome_halves(d: int) -> list[str]:
    """Get the halves of a palindrome with d digits rounded down."""
    half_digit = d // 2
    return [str(x) for x in range(10 ** (half_digit - 1), 10**half_digit)]


def get_palindromes(n: int) -> list[int]:
    """Get a list of palindromes less than n."""
    palindromes = [x for x in range(10)]
    for d in range(2, len(str(n)) + 1):
        half = get_palindrome_halves(d)
        if d % 2 == 0:
            palindromes.extend(int(n + n[::-1]) for n in half)
        else:
            for i in range(10):
                palindromes.extend(int(n + str(i) + n[::-1]) for n in half)
    return [p for p in palindromes if p < n]


def is_binary_palindrome(n: int) -> bool:
    """Returns True if n is a palindrome in base and False otherwise."""
    binary = bin(n)[2:]
    return binary == binary[::-1]


def sum_double_base_palindromes(n: int) -> int:
    """Get the sum of all numbers that are palindromes in base 2 and 10."""
    palindromes = get_palindromes(n)
    return sum(p for p in palindromes if is_binary_palindrome(p))
