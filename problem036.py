import numpy as np

def get_num_str(x, d):
    n = str(x)
    if len(n) == d:
        return n
    else:
        n = "0"*(d-len(n))+n
        return n

def get_nums(d: int) -> str:
    nums = list(get_num_str(x, d) for x in range(10**d) if x % 10 != 0)
    return nums

def get_palindromes(N):
    # Single digit palindromes
    palindromes = [x for x in range(10)]
    for d in range(2, len(str(N))+1):
        # if d is even
        if d % 2 == 0:
            nums = get_nums(d//2)
            palindromes += [int(n[::-1]+n) for n in nums]
        # If d is odd
        else:
            nums = get_nums((d-1)//2)
            for i in range(10):
                palindromes += [int(n[::-1]+str(i)+n) for n in nums]
    palindromes = np.array(palindromes, dtype="int64")
    palindromes = palindromes[palindromes < N]
    return palindromes

def get_double_palindrome_sum(N):
    # Get all Palindromes < N
    palindromes = get_palindromes(N)
    psum = 0
    for p in palindromes:
        # Get Binary form of palindrome
        digits = []
        n = p
        if n == 0:
            digits.append(0)
        while n != 0:
            digits.append(n % 2)
            n //= 2
        # Check if bindary number is palindrome
        p_binary = "".join(str(d) for d in digits)
        if p_binary == p_binary[::-1]:
            psum += p
    return psum

print(get_double_palindrome_sum(1000000))