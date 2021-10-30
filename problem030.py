def get_5pow_digit_sum(x: int) -> int:
    s = sum(int(d)**5 for d in str(x))
    return s

def get_sum_digit_5pow(N: int) -> list:
    nums = []
    for x in range(2, N):
        if get_5pow_digit_sum(x) == x:
            nums.append(x)
    return sum(nums)

# max 6 digits because 7*9^5 has 6 digits
print(get_sum_digit_5pow(1000000))