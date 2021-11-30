with open("p079_keylog.txt","r") as f:
    logins = tuple(tuple(int(d) for d in n) for n in f.read().split("\n")[:-1])

def dfs_traverse(passcodes, passcode, right_adj, d):
    if d not in right_adj:
        passcodes.append(passcode)
        return
    else:
        for next_d in right_adj[d]:
            dfs_traverse(passcodes, passcode*10+next_d, right_adj, next_d)

def generate_shortest_passcodes(logins):
    right_adj = {}
    # Initial right adjacent digits
    for n in logins:
        for i in range(len(n)-1):
            if n[i] not in right_adj:
                right_adj[n[i]] = {n[i+1]}
            else:
                right_adj[n[i]].add(n[i+1])
    # Remove non-adjacent digits
    for n in logins:
        if n[2] in right_adj[n[0]]:
            right_adj[n[0]].remove(n[2])
    # Get the first digit
    A = set(d for d in right_adj.keys())
    B = set(d for dset in right_adj.values() for d in dset)
    C = [d for d in A if d not in B]
    # Traverse graph to get passcodes
    passcodes = []
    dfs_traverse(passcodes, C[0], right_adj, C[0])
    # Check passcode contains all digits; return first instance
    dset = A | B
    for passcode in passcodes:
        if set(int(d) for d in str(passcode)) == dset:
            return passcode
