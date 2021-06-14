import numpy as np

def get_primes(n):
    numbers = np.arange(n+1, dtype=np.int64)
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2,(n+1)//i+1):
                if j*i <= n:
                    is_prime[j*i] = False
        else:
            continue
    return numbers[is_prime]

def is_odd_digit_over2(n):
    is_odo = True
    if n < 100:
        return True
    while n != 0:
        if n % 2 == 0:
            is_odo = False
            break
        n //= 10
    return is_odo

PRIMES = get_primes(1000000)
PRIMES_NO_EVENS = PRIMES[[is_odd_digit_over2(p) for p in PRIMES]]
SINGLE_TRUNC_PRIMES = {2, 3, 5, 7}

def is_left_truncatable(p):
    str_p = str(p)
    for j in range(1,len(str_p)):
        new_p = int(str_p[j:])
        if new_p not in PRIMES:
            return False
    else:
        return True
    
def is_right_truncatable(p):
    str_p = str(p)
    for j in range(1,len(str_p)):
        new_p = int(str_p[:-j])
        if new_p not in PRIMES:
            return False
    else:
        return True

def find_truncatable_primes_sum():
    ltp = PRIMES_NO_EVENS[list(is_left_truncatable(p) for p in PRIMES_NO_EVENS)]
    rtp = PRIMES_NO_EVENS[list(is_right_truncatable(p) for p in PRIMES_NO_EVENS)]
    return sum(set(ltp) & set(rtp) - SINGLE_TRUNC_PRIMES)

print(find_truncatable_primes_sum())