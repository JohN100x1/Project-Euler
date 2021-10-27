def get_lychrel_count(N):
    count = 0
    for x in range(1, N):
        for iterations in range(50):
            x += int(str(x)[::-1])
            if str(x) == str(x)[::-1]:
                break
        else:
            count += 1
    return count

print(get_lychrel_count(10000))