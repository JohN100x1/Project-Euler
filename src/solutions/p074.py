from config import DIGIT_FACTORIALS


def count_chains_with_length(length: int, max_n: int) -> int:
    """Get the number of digit factorial sum chains with 60 non-repeating."""
    chain: dict[int, int] = {}
    count = 0
    for n0 in range(max_n):
        n = n0
        sub_chain = {}
        sub_count = 0
        # Get the next terms of the digit factorial sum until it hits a chain
        while n not in chain and n not in sub_chain:
            sub_chain[n] = sub_count
            sub_count += 1
            n = sum(DIGIT_FACTORIALS[d] for d in str(n))
        # If the latest value is in the chain, add all values from sub-chain
        if n in chain:
            for i, m in enumerate(reversed(sub_chain), 1):
                chain[m] = chain[n] + i
        # If it's in the sub-chain, calculate the length of the period
        elif n in sub_chain:
            for i, m in enumerate(sub_chain):
                if i >= sub_chain[n]:
                    chain[m] = sub_count - sub_chain[n]
                else:
                    chain[m] = len(sub_chain) - i
        if chain[n0] >= length:
            count += 1
    return count
