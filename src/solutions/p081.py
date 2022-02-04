import numpy as np

MATRIX = np.loadtxt("p081_matrix.txt", dtype=np.int32, delimiter = ",")

def get_two_way_min_path_sum():
    ubound = MATRIX.shape[0] + MATRIX.shape[1] - 2
    halfway = (MATRIX.shape[0] + MATRIX.shape[1])//2
    psums1 = [MATRIX[-1][-1]]
    for i in range(ubound, 0, -1):
        psums1, psums2 = [], psums1
        diag = np.diag(MATRIX[::-1,:], i-MATRIX.shape[0])
        uboundj = len(diag) - 1
        if i >= halfway:
            for j, n in enumerate(diag):
                if j == 0:
                    psum = diag[j]+psums2[j]
                elif j == uboundj:
                    psum = diag[j]+psums2[j-1]
                else:
                    sum1 = diag[j]+psums2[j-1]
                    sum2 = diag[j]+psums2[j]
                    psum = min(sum1, sum2)
                psums1.append(psum)
        else:
            for j, n in enumerate(diag):
                sum1 = diag[j]+psums2[j]
                sum2 = diag[j]+psums2[j+1]
                psums1.append(min(sum1, sum2))
    return psums1[0]

print(get_two_way_min_path_sum())