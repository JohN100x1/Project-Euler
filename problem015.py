from scipy.special import binom

def get_lattice_paths(n: int) -> int:
    num_paths = 0
    for j in range(n+1):
        num_paths += binom(n,j)**2
    return int(num_paths)

print(get_lattice_paths(20))