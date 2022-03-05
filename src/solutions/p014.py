def get_next_collatz(n: int) -> int:
    """Get next number in Collatz sequence."""
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def get_chain_len(n: int, chain_len: dict) -> int:
    """Get chain length of n recursively."""
    if n not in chain_len:
        chain_len[n] = 1 + get_chain_len(get_next_collatz(n), chain_len)
    return chain_len[n]


def get_longest_collatz_seq(max_n: int) -> int:
    """Get maximum chain length for starting integer n < max_n."""
    chain_len = {1: 1}
    for n in range(2, max_n):
        chain_len[n] = get_chain_len(n, chain_len)
    return max(chain_len, key=chain_len.get)
