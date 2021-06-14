def find_coin_comb(coins: list, S: int) -> int:
    # Case with 1p and 2p coins
    if len(coins) == 2:
        ways = S//2 + 1
        return ways
    # Fix number of largest coin and find number of ways in smaller batch
    else:
        big_coin = max(coins)
        new_coins = [c for c in coins if c != big_coin]
        ways = sum(find_coin_comb(new_coins, S-k*big_coin) for k in range(0,S//big_coin+1))
        return ways

print(find_coin_comb([1,2,5,10,20,50,100,200],200))