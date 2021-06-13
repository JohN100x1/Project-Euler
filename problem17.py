digits = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
over20 = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

def get_num_letters(x):
    assert(len(str(x)) <= 3)
    y = [int(d) for d in str(x)[::-1]]
    # letters 1-9
    if len(y) == 1:
        return digits[y[0]]
    # Letters 10-99
    if len(y) == 2:
        # If tens are in the teens
        if y[1] == 1:
            return teens[y[0]+y[1]*10]
        else:
            return digits[y[0]] + over20[y[1]]
    # Letters for the hundreds digit
    if len(y) == 3:
        hundreds = digits[y[2]] + 7
    else:
        hundreds = 0
    # Count letters
    if y[0] == 0 and y[1] == 0:
        return hundreds
    else:
        # If tens are in the teens
        if y[1] == 1:
            return teens[y[0]+y[1]*10] + 3 + hundreds
        else:
            return digits[y[0]] + over20[y[1]] + 3 + hundreds

def get_total_letters1000():
    s = 11
    for i in range(1,1000):
        s += get_num_letters(i)
    return s

print(get_total_letters1000())