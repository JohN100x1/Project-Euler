def get_fib_even_sum(n: int) -> int:
    esum = 0
    Fa, Fb = 1, 1
    while Fb < n:
        Fa, Fb = Fb, Fa+Fb
        if Fb % 2 == 0:
            esum += Fb
    return esum

print(get_fib_even_sum(4000000))