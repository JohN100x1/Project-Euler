class FiveGon:
    """Get the maximum integer formed by the 5-gon string with numbers 1-10."""

    LINE_INDEXES = {
        0: (1, 2),
        1: (0, 2),
        2: (0, 1),
        3: (2, 4),
        4: (2, 3),
        5: (4, 6),
        6: (4, 5),
        7: (6, 8),
        8: (6, 7),
        9: (1, 8),
    }
    IN_NODES = {1, 2, 4, 6, 8}

    def __init__(self):
        self.list_five_gon = []
        self.five_gon = [0 for _ in range(10)]

    @staticmethod
    def get_five_gon_string(five_gon: list[int]) -> str:
        """Get the integer string for a given 5-gon."""
        lines = [
            str(five_gon[0]) + str(five_gon[1]) + str(five_gon[2]),
            str(five_gon[3]) + str(five_gon[2]) + str(five_gon[4]),
            str(five_gon[5]) + str(five_gon[4]) + str(five_gon[6]),
            str(five_gon[7]) + str(five_gon[6]) + str(five_gon[8]),
            str(five_gon[9]) + str(five_gon[8]) + str(five_gon[1]),
        ]
        out_nodes = {i: five_gon[j] for i, j in enumerate((0, 3, 5, 7, 9))}
        min_idx = min(out_nodes, key=out_nodes.get)
        return "".join(lines[(i + min_idx) % 5] for i in range(5))

    def is_possible(self, idx: int, v: int) -> bool:
        """Check if a node idx can contain the value v for the 5-gon."""
        # Check inner nodes don't contain a 10
        if v == 10 and idx in self.IN_NODES:
            return False
        line_sum = 0
        # Don't check line sum if any other of the line node is 0
        for j in self.LINE_INDEXES[idx]:
            if self.five_gon[j] == 0:
                return True
            line_sum += self.five_gon[j]
        # Check line sum equals 14
        # The line sum which gives max digits is 14
        # because 6,7,8,9,10 must be in the outer nodes
        if v + line_sum == 14:
            return True
        return False

    def solve_five_gon(self, nums: set[int]):
        """Recursively fill out possible values on the 5-gon."""
        for i in range(10):
            if self.five_gon[i] == 0:
                for v in nums:
                    if self.is_possible(i, v):
                        self.five_gon[i] = v
                        self.solve_five_gon(nums - {v})
                        self.five_gon[i] = 0
                return
        self.list_five_gon.append(self.five_gon.copy())

    def get_five_gon_max_num(self) -> int:
        """Get the maximum integer formed by the 5-gon."""
        max_num = 0
        if len(self.list_five_gon) == 0:
            self.solve_five_gon({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
        for five_gon in self.list_five_gon:
            five_gon_string = self.get_five_gon_string(five_gon)
            if int(five_gon_string) > max_num:
                max_num = int(five_gon_string)
        return max_num
