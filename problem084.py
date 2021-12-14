import numpy as np

def get_monopoly_transition_matrix():
    ### WARNING: This solution doesn't account for the 3 doubles rule!
    ### WARNING: This solution doesn't account for the 3 doubles rule!
    ### WARNING: This solution doesn't account for the 3 doubles rule!
    ### WARNING: Expand transition matrix to 120x120 at a later date!
    ### WARNING: Expand transition matrix to 120x120 at a later date!
    ### WARNING: Expand transition matrix to 120x120 at a later date!
    eps = pow(10, -6)
    community_chests = {2, 17, 33}
    chances = {7:(15,12), 22:(25,28), 36:(5,12)}
    # n-sided dice numbered 1 to n <= 38
    n = 4
    # Roll probabilities for n-sided dice
    roll_probs = np.zeros(40)
    for i, j in enumerate(range(1, 2*n), 2):
        roll_probs[i] = (n-abs(j-n))/n**2
    # Monopoly Transition matrix
    M = np.zeros((40, 40))
    for i in range(40):
        M[i,:] = np.roll(roll_probs, i)
    # Go to Jail square
    M[30, :] = 0
    M[30, 10] = 1
    # Reroute lands on the Go to Jail square to Jail
    for i in range(40):
        M[i, 10] += M[i, 30]
        M[i, 30] = 0
    # Community Chest reroutes
    for i in range(40):
        for j in community_chests:
            if M[i, j] > eps:
                M[i, 0] += M[i, j]/16
                M[i,10] += M[i, j]/16
                M[i, j] *= 7/8
    # Chane reroutes
    for i in range(40):
        for j in chances:
            R, U = chances[j]
            if M[i, j] > eps:
                M[i, 0] += M[i, j]/16
                M[i,10] += M[i, j]/16
                M[i,11] += M[i, j]/16
                M[i,24] += M[i, j]/16
                M[i,39] += M[i, j]/16
                M[i, 5] += M[i, j]/16
                M[i, R] += M[i, j]/8
                M[i, U] += M[i, j]/16
                M[i,j-3] += M[i,j]/16
                M[i, j] *= 3/8
    return M

def get_modal_string(d):
    assert(d % 2 == 0)
    initial = np.array([1]+[0 for _ in range(39)])
    M = get_monopoly_transition_matrix()
    modal_idx = np.argsort(initial.dot(np.linalg.matrix_power(M, 1000)))
    modal_string = 0
    for i, idx in enumerate(reversed(modal_idx), 1):
        modal_string *= 100
        modal_string += idx
        if i % (d // 2) == 0:
            break
    return modal_string

print(get_modal_string(6))