with open("p022_names.txt") as f:
    NAMES = f.read().replace("\"","").split(",")

def name_score(pos, name):
    score = pos * sum(ord(letter)-64 for letter in name)
    return score

def get_total_score():
    total_score = 0
    sorted_names = sorted(NAMES)
    for pos, name in enumerate(sorted_names):
        total_score += name_score(pos+1, name)
    return total_score

print(get_total_score())