def largest_palindrome():
    palindrome = 0
    for i in range(999,100,-1):
        for j in range(999,i,-1):
            k = i*j
            if str(k) == str(k)[::-1] and k >= palindrome:
                palindrome = k
    return palindrome

print(largest_palindrome())