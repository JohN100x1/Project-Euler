import numpy as np


def get_monopoly_transition_matrix() -> np.array:
    """
    Get the transition matrix for the monopoly board.

    WARNING: This solution doesn't account for the 3 doubles rule!
    TODO: Expand transition matrix to 120x120 at a later date!
    """
    eps = pow(10, -6)
    community_chests = {2, 17, 33}
    chances = {7: (15, 12), 22: (25, 28), 36: (5, 12)}
    # n-sided dice numbered 1 to n <= 38
    n = 4
    # Roll probabilities for n-sided dice
    roll_probs = np.zeros(40)
    for i, j in enumerate(range(1, 2 * n), 2):
        roll_probs[i] = (n - abs(j - n)) / n**2
    # Monopoly Transition matrix
    matrix = np.zeros((40, 40))
    for i in range(40):
        matrix[i, :] = np.roll(roll_probs, i)
    # Go to Jail square
    matrix[30, :] = 0
    matrix[30, 10] = 1
    # Reroute lands on the Go-to Jail square to Jail
    for i in range(40):
        matrix[i, 10] += matrix[i, 30]
        matrix[i, 30] = 0
    # Community Chest reroutes
    for i in range(40):
        for j in community_chests:
            if matrix[i, j] > eps:
                matrix[i, 0] += matrix[i, j] / 16
                matrix[i, 10] += matrix[i, j] / 16
                matrix[i, j] *= 7 / 8
    # Chance reroutes
    for i in range(40):
        for j in chances:
            r, u = chances[j]
            if matrix[i, j] > eps:
                matrix[i, 0] += matrix[i, j] / 16
                matrix[i, 10] += matrix[i, j] / 16
                matrix[i, 11] += matrix[i, j] / 16
                matrix[i, 24] += matrix[i, j] / 16
                matrix[i, 39] += matrix[i, j] / 16
                matrix[i, 5] += matrix[i, j] / 16
                matrix[i, r] += matrix[i, j] / 8
                matrix[i, u] += matrix[i, j] / 16
                matrix[i, j - 3] += matrix[i, j] / 16
                matrix[i, j] *= 3 / 8
    return matrix


def get_modal_string() -> int:
    """
    Get the Modal string of the 3 most probable monopoly squares to be in.
    """
    initial = np.array([1] + [0 for _ in range(39)])
    matrix = get_monopoly_transition_matrix()
    modal_idx = np.argsort(initial.dot(np.linalg.matrix_power(matrix, 1000)))
    modal_string = 0
    for i, idx in enumerate(reversed(modal_idx), 1):
        modal_string *= 100
        modal_string += idx
        if i % 3 == 0:
            break
    return modal_string
