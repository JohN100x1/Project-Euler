def sum_coin_combinations(target: int, coins: list[int]) -> int:
    """Get a combination of the ways coins can sum up to target."""
    ways = [1] + [0] * target
    for coin in coins:
        for value in range(coin, target + 1):
            ways[value] += ways[value - coin]
    return ways[target]
