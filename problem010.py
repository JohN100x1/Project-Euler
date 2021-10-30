def get_prime_sum(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return 2 + sum(i for i in range(3,n,2) if sieve[i])

print(get_prime_sum(2000000))