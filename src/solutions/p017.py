SUB20_LETTERS = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
                 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
OVR20_LETTERS = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

def get_num_letters(x):
    # Letters 1-1000
    hundreds = SUB20_LETTERS[x//100] + 7
    if x < 100:
        hundreds = 0
    elif x % 100 == 0:
        if x == 1000:
            return SUB20_LETTERS[x//1000] + 8
        return hundreds
    else:
        hundreds += 3
    if x % 100 < 20:
        return SUB20_LETTERS[x%100] + hundreds
    return SUB20_LETTERS[x%10] + OVR20_LETTERS[(x%100)//10] + hundreds

def get_letter_sum(n):
    lsum = 0
    for i in range(1,n+1):
        lsum += get_num_letters(i)
    return lsum

print(get_letter_sum(1000))