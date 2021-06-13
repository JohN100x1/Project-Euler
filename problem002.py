def fibonacci_even_sum(n: int) -> int:
    # n is the n-th even term in the fibonacci sequence
    # There are 11 even terms before fibonacci > 4 million
    # Use closed form for fibonacci term
    # Apply geometric series sum
    phi3 = (0.5*(1+5**0.5))**3
    psi3 = (0.5*(1-5**0.5))**3
    # Fn = (phi**n - psi**n)/5**0.5
    Sn = (phi3*(1-phi3**n)/(1-phi3)-psi3*(1-psi3**n)/(1-psi3))/5**0.5
    return int(Sn)

print(fibonacci_even_sum(11))