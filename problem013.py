import numpy as np

NUMBERS = np.loadtxt("p013_numbers.txt")

def get_first_ten_digits():
    ftd = np.sum(NUMBERS)
    ftd = int(str(ftd).replace('.', '')[:10])
    return ftd

print(get_first_ten_digits())