# Greedy way
def find_coins_greedy(amount, coins):
    result = {}

    for coin in sorted(coins, reverse=True):
        count = amount // coin #how many of this coin
        if count > 0:
            result[coin] = count
            amount -= coin * count # reduce 
            
    return result


print(find_coins_greedy(113, [50, 25, 10, 5, 2, 1]))
print(find_coins_greedy(6, [1, 3, 4]))


# Dynamic programming way
def find_min_coins(amount, coins):
    memo = {0: 0}
    coin_used = {}

    for i in range(1, amount + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            if memo.get(subproblem) is not None:
                candidate = memo[subproblem] + 1
                if memo.get(i) is None or candidate < memo[i]:
                    memo[i] = candidate
                    coin_used[i] = coin
       
    result = {}
    current = amount
    while current > 0:
        coin = coin_used.get(current)
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

print(find_min_coins(113, [50, 25, 10, 5, 2, 1]))
print(find_min_coins(6, [1, 3, 4]))


# def find_min_coins(amount):
#     coins = [50, 25, 10, 5, 2, 1] 
#     dp = [float('inf')] * (amount + 1)
#     coin_used = [0] * (amount + 1)

#     dp[0] = 0 # 0 coins needed for amount 0

#     for coin in coins:
#         for i in range(coin, amount + 1):
#             if dp[i - coin] + 1 < dp[i]:
#                 dp[i] = dp[i - coin] + 1
#                 coin_used[i] = coin

#     # Backtrack to find which coins were used
#     result = {}
#     while amount > 0:
#         coin = coin_used[amount]
#         result[coin] = result.get(coin, 0) + 1
#         amount -= coin

#     return result

# print(find_min_coins(113))
   


