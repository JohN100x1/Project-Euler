import numpy as np

GRID = np.loadtxt("p011_grid.txt", dtype=np.int64)

def get_largest_prod():
    product = 1
    n = GRID.shape[0]
    # row product
    for i in range(n):
        for j in range(n-4):
            p = np.prod(GRID[i,j:j+4])
            if p >= product:
                product = p
    # column product
    for i in range(n-4):
        for j in range(n):
            p = np.prod(GRID[i:i+4,j])
            if p >= product:
                product = p
    dx = np.array([0,1,2,3])
    # left diagonal product
    for i in range(n-4):
        for j in range(n-4):
            p = np.prod(GRID[i+dx,j+dx])
            if p >= product:
                product = p
    # right diagonal product
    for i in range(3, n):
        for j in range(n-4):
            p = np.prod(GRID[i-dx,j+dx])
            if p >= product:
                product = p
    return int(product)

print(get_largest_prod())