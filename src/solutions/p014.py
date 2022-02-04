def get_next_collatz(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1

def get_chain_len(n, chain_len):
    if n in chain_len.keys():
        return chain_len[n]
    else:
        cl = 1 + get_chain_len(get_next_collatz(n), chain_len)
        chain_len[n] = cl
        return cl

def get_longest_collatz_seq(N):
    chain_len = {1:1}
    for n in range(2, N):
        chain_len[n] = get_chain_len(n, chain_len)
    return max(chain_len, key=chain_len.get)

print(get_longest_collatz_seq(1000000))