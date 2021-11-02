def get_e_denom(n):
    if n == 1:
        return 2
    elif n % 3 == 0:
        return 2*(n // 3)
    else:
        return 1

def get_e_convergent(n):
    denom = 1
    numer = get_e_denom(n)
    for k in range(1, n):
        numer, denom = numer*get_e_denom(n-k)+denom, numer
    return (numer, denom)

def get_e_convergent_numer_digit_sum(n):
    numer, denom = get_e_convergent(n)
    return sum(map(int, str(numer)))

print(get_e_convergent_numer_digit_sum(100))