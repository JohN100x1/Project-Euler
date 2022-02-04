class Fivegon():
    LINE_IDXS = {
        0:(1,2),
        1:(0,2),
        2:(0,1),
        3:(2,4),
        4:(2,3),
        5:(4,6),
        6:(4,5),
        7:(6,8),
        8:(6,7),
        9:(1,8)
        }
    IN_NODES = {1, 2, 4, 6, 8}
    def __init__(self):
        self.fivegons = []
        self.fivegon = [0 for i in range(10)]
    def is_possible(self, i, v):
        # Check inner nodes don't contain a 10
        if v == 10 and i in Fivegon.IN_NODES:
            return False
        lsum = 0
        # Don't check line sum if any other of the line node is 0
        for j in Fivegon.LINE_IDXS[i]:
            if self.fivegon[j] == 0:
                return True
            lsum += self.fivegon[j]
        # Check line sum equals 14
        # The line sum which gives max digits is 14
        # because 6,7,8,9,10 must be in the outer nodes
        if v + lsum == 14:
            return True
        else:
            return False
    def solve_fivegon(self, nlist):
        for i in range(10):
            if self.fivegon[i] == 0:
                for v in nlist:
                    if self.is_possible(i, v):
                        self.fivegon[i] = v
                        self.solve_fivegon(nlist - {v})
                        self.fivegon[i] = 0
                return
        self.fivegons.append(self.fivegon.copy())
    def get_fivegon_string(self, fgon):
        dset = []
        dset.append(str(fgon[0])+str(fgon[1])+str(fgon[2]))
        dset.append(str(fgon[3])+str(fgon[2])+str(fgon[4]))
        dset.append(str(fgon[5])+str(fgon[4])+str(fgon[6]))
        dset.append(str(fgon[7])+str(fgon[6])+str(fgon[8]))
        dset.append(str(fgon[9])+str(fgon[8])+str(fgon[1]))
        out_nodes = {i:fgon[j] for i,j in enumerate((0,3,5,7,9))}
        min_idx = min(out_nodes, key=out_nodes.get)
        fivegon_string = ""
        for i in range(5):
            fivegon_string += dset[(i+min_idx) % 5]
        return fivegon_string
    def get_fivegon_max_num(self):
        max_num = 0
        if len(self.fivegons) == 0:
            self.solve_fivegon({1,2,3,4,5,6,7,8,9,10})
        for fivegon in self.fivegons:
            fivegon_string = self.get_fivegon_string(fivegon)
            if int(fivegon_string) > max_num:
                max_num = int(fivegon_string)
        return max_num

new_fivegon = Fivegon()
print(new_fivegon.get_fivegon_max_num())

    
    