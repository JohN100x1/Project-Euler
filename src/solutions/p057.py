def get_sqrt2_continued_fraction_digit_count(N):
    count = 0
    numers = [1]
    denoms = [2]
    for i in range(N + 1):
        numer = denoms[-1]
        denom = 2*denoms[-1] + numers[-1]
        numers[-1] = numer + denom
        if len(str(numers[-1])) > len(str(denom)):
            count += 1
        numers.append(numer)
        denoms.append(denom)
    return count

print(get_sqrt2_continued_fraction_digit_count(1000))