# Digit Factorials
DFACTORIALS = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def get_dfsum(x):
    return sum(DFACTORIALS[int(d)] for d in str(x))

def get_equal_dfsums(N):
    digit_factorials = set()
    for i in range(3, N+1):
        if get_dfsum(i) == i:
            digit_factorials.add(i)
    return digit_factorials

print(sum(get_equal_dfsums(50000)))
