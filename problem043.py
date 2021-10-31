def get_3_digit_multiples(k):
    umults = []
    multiples = [j for j in range(k,1000,k) if j > 10]
    for m in multiples:
        mult = str(m)
        # Add zero if only 2-digits
        if len(mult) == 2:
            mult = "0"+mult
        # Check if digits are unique
        if len(mult) == len(set(mult)):
            umults.append(mult)
    return umults

def get_substring_div_sum():
    digits = {str(j) for j in range(10)}
    divs = [17, 13, 11, 7, 5, 3, 2]
    candidates = get_3_digit_multiples(17)
    for i in range(1, len(divs)):
        follow_up = get_3_digit_multiples(divs[i])
        possible_values = []
        for c in candidates:
            for f in follow_up:
                if f[1:] == c[:2]:
                    possible_values.append(f[0]+c)
        candidates = possible_values
    # Remove leading zeros candidates
    candidates = [c for c in candidates if c[0] != "0"]
    # Remove Repeating digit candidates
    candidates = [c for c in candidates if len(c) == len(set(c))]
    # Place remaining digit d1 since d1 is bounded only pandigitality
    psum = 0
    for c in candidates:
        (d, ) = digits - set(c)
        psum += int(d+c)
    return psum

print(get_substring_div_sum())