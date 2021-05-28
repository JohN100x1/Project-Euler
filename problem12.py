def triangle_number(n: int) -> int:
    Tn = 0.5*n*(n+1)
    return int(Tn)

def get_num_divisors(num: int) -> int:
    if num == 1:
        return 1
    else:
        num_divisors = 2
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                num_divisors += 2
        return num_divisors

def high_divisible_Tn(m: int, maxn: int) -> int:
    for n in range(1, maxn+1):
        Tn = triangle_number(n)
        num_divisors = get_num_divisors(Tn)
        if num_divisors > m:
            break
    return int(Tn)

print(high_divisible_Tn(500, 99999))