def split_lines(lines):
    num_list = []
    for line in lines.split("\n"):
        num_list.append([int(n) for n in line.split(" ")])
    return num_list

with open("p018_numbers.txt","r") as f:
    PATHS = split_lines(f.read())

def get_max_path():
    n = len(PATHS)
    for i in range(n-2,-1,-1):
        for j in range(len(PATHS[i])):
            PATHS[i][j] += max(PATHS[i+1][j],PATHS[i+1][j+1])
    return PATHS[0][0]

print(get_max_path())