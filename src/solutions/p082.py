import numpy as np

MATRIX = np.loadtxt("p081_matrix.txt", dtype=np.int32, delimiter = ",")

def get_three_way_min_path_sum():
    height = MATRIX.shape[0]
    psums1 = list(MATRIX[:,-1])
    for i in range(len(MATRIX)-2, -1, -1):
        psums1, psums2 = [], psums1
        col = MATRIX[:,i]
        for j in range(height):
            sums = []
            for k in range(height):
                if k < j:
                    csum = sum(col[k:j+1])
                elif k > j:
                    csum = sum(col[j:k+1])
                else:
                    csum = col[k]
                sums.append(csum + psums2[k])
            psums1.append(min(sums))
    return min(psums1)

print(get_three_way_min_path_sum())