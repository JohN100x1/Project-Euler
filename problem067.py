def split_lines(lines):
    num_list = []
    for line in lines.split("\n"):
        num_list.append([int(n) for n in line.split(" ")])
    return num_list

with open("problem67_numbers.txt","r") as f:
    paths = split_lines(f.read())

def get_max_path():
    n = len(paths)
    for i in range(n-2,-1,-1):
        for j in range(len(paths[i])):
            paths[i][j] += max(paths[i+1][j],paths[i+1][j+1])
    return paths[0][0]

print(get_max_path())