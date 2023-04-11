import itertools

from utils.exceptions import SolutionNotFoundError


def get_partition_divisible_by(d: int) -> int:
    """
    Get the smallest n such that the number of partitions of n is divided by d.

    NOTE: Not my solution, Source: https://github.com/TheAlgorithms/Python/
    """
    partitions = [1]

    for i in itertools.count(len(partitions)):
        item = 0
        for j in itertools.count(1):
            sign = -1 if j % 2 == 0 else +1
            index = (j * j * 3 - j) // 2
            if index > i:
                break
            item = (item + partitions[i - index] * sign) % d
            index += j
            if index > i:
                break
            item = (item + partitions[i - index] * sign) % d

        if item == 0:
            return i
        partitions.append(item)
    raise SolutionNotFoundError("Failed to solve p078.")
