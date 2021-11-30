from decimal import getcontext, Decimal

def get_sqrt_digit_sum(n):
    getcontext().prec = 105
    return sum(Decimal(n).sqrt().as_tuple()[1][:100])
    
def get_sqrt_digit_sums(N):
    sqnums = {n**2 for n in range(1, int(N**0.5)+1)}
    dsums = 0
    for n in range(1, N+1):
        if n in sqnums:
            continue
        dsums += get_sqrt_digit_sum(n)
    return dsums

print(get_sqrt_digit_sums(100))