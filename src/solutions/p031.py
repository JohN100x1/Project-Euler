def count_coin_sum_comb(coins: list, coin_sum: int) -> int:
    """Get the number of ways the list of coins can make the coin_sum."""
    # Case with 1p and 2p coins
    if len(coins) == 2:
        ways = coin_sum // 2 + 1
        return ways
    # Fix number of the biggest coins and find number of ways in smaller batch
    else:
        big_coin = max(coins)
        new_coins = [c for c in coins if c != big_coin]
        ways = sum(
            count_coin_sum_comb(new_coins, coin_sum - k * big_coin)
            for k in range(0, coin_sum // big_coin + 1)
        )
        return ways
