def get_palindrome_halfs(d: int) -> str:
    nums = [str(x) for x in range(10**(d-1), 10**d)]
    return nums

def get_palindromes(N):
    # Single digit palindromes
    palindromes = [x for x in range(10)]
    for d in range(2, len(str(N))+1):
        # if d is even
        if d % 2 == 0:
            halfs = get_palindrome_halfs(d//2)
            palindromes += [int(n+n[::-1]) for n in halfs]
        # If d is odd
        else:
            halfs = get_palindrome_halfs((d-1)//2)
            for i in range(10):
                palindromes += [int(n+str(i)+n[::-1]) for n in halfs]
    palindromes = [p for p in palindromes if p < N]
    return palindromes

def get_double_palindrome_sum(N):
    # Get all Palindromes < N
    palindromes = get_palindromes(N)
    psum = 0
    for p in palindromes:
        # Get Binary form of palindrome
        binary = bin(p)[2:]
        # Check if bindary number is palindrome
        if binary == binary[::-1]:
            psum += p
    return psum

print(get_double_palindrome_sum(1000000))