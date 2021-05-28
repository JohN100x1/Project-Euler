import numpy as np

grid = np.loadtxt("problem11_grid.txt")

def find_largest_4prod():
    product = 1
    n = grid.shape[0]
    # row product
    for i in range(n):
        for j in range(n-4):
            p = np.prod(grid[i,j:j+4])
            if p >= product:
                product = p
    # column product
    for i in range(n-4):
        for j in range(n):
            p = np.prod(grid[i:i+4,j])
            if p >= product:
                product = p
    dx = np.array([0,1,2,3])
    # left diagonal product
    for i in range(n-4):
        for j in range(n-4):
            p = np.prod(grid[i+dx,j+dx])
            if p >= product:
                product = p
    # right diagonal product
    for i in range(3, n):
        for j in range(n-4):
            p = np.prod(grid[i-dx,j+dx])
            if p >= product:
                product = p
    return int(product)

print(find_largest_4prod())