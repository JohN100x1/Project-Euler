import numpy as np

MATRIX = np.loadtxt("p081_matrix.txt", dtype=np.int32, delimiter = ",")

def get_adj(m, n, visited, w):
    adj_nodes = set()
    north = (w[0]-1, w[1])
    south = (w[0]+1, w[1])
    west = (w[0], w[1]-1)
    east = (w[0], w[1]+1)
    if 0 < w[0] and north not in visited:
        adj_nodes.add(north)
    if w[0] < m-1 and south not in visited:
        adj_nodes.add(south)
    if 0 < w[1] and west not in visited:
        adj_nodes.add(west)
    if w[1] < n-1 and east not in visited:
        adj_nodes.add(east)
    return adj_nodes

def dijkstra(M, source, end):
    m, n = M.shape
    psums1 = {}
    psums1[source] = M[source]
    psums2 = {}
    while end not in psums2:
        w = min(psums1, key=psums1.get)
        psums2[w] = psums1[w]
        del psums1[w]
        for x in get_adj(m, n, psums2, w):
            if x not in psums1:
                psums1[x] = psums2[w] + M[x]
            elif psums2[w] + M[x] < psums1[x]:
                psums1[x] = psums2[w] + M[x]
    return psums2[end]

def get_four_way_min_path_sum():
    return dijkstra(MATRIX, (0,0), (MATRIX.shape[0]-1,MATRIX.shape[1]-1))

print(get_four_way_min_path_sum())