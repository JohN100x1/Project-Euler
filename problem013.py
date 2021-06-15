import numpy as np

numbers = np.loadtxt("problem013_numbers.txt")

def first_ten_digits():
    ftd = np.sum(numbers)
    ftd = int(str(ftd).replace('.', '')[:10])
    return ftd