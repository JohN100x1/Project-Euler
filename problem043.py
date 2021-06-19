def get_3d_mults(k):
    umults = []
    mults = [j for j in range(k,1000,k) if j > 10]
    for i, j in enumerate(mults):
        str_j = str(j)
        # Add zero if only 2-digits
        if len(str_j) == 2:
            str_j = "0"+str_j
        # Check if digits are unique
        if len(str_j) == len(set(str_j)):
            umults.append(str_j)
    return umults

def find_substring_div_sum():
    divs = [17, 13, 11, 7, 5, 3, 2]
    candidates = get_3d_mults(17)
    for i in range(1, len(divs)):
        follow_up = get_3d_mults(divs[i])
        possible_values = []
        for c in candidates:
            for f in follow_up:
                if f[1:] == c[:2]:
                    possible_values.append(f[0]+c)
        candidates = possible_values.copy()
    # Remove leading zeros candidates
    candidates = [c for c in candidates if c[0] != "0"]
    # Remove Repeating digit candidates
    candidates = [c for c in candidates if len(c) == len(set(c))]
    # Place remaining digit
    digit09 = {str(j) for j in range(10)}
    for i, c in enumerate(candidates):
        (d, ) = digit09 - set(c)
        candidates[i] = d+c
    substring_div_sum = sum(int(n) for n in candidates)
    return substring_div_sum

print(find_substring_div_sum())