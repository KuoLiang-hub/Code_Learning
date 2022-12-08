"""
A greedy algorithm is an algorithmic strategy that makes the locally optimal choice at each step 
with the hope of finding a global optimum. Here is an example of a greedy algorithm in python to solve the 
problem of finding the minimum number of coins to give as change:
"""

def minCoins(coins, total):
    # list to store the minimum number of coins needed
    # to make the change
    min_coins = [0] * (total + 1)

    # iterate through all the possible values of change
    for i in range(1, total+1):
        min_value = float('inf')
        for coin in coins:
            if i >= coin:
                min_value = min(min_value, 1 + min_coins[i-coin])
        min_coins[i] = min_value

    return min_coins[total]
    
"""The function minCoins() takes in a list of coins and the total amount of change we 
need to make as input. It then iterates through all the possible values of change and 
for each value, it considers using each coin to make the change. It chooses the coin 
that minimizes the number of coins needed to make the change and updates the minimum 
number of coins needed to make the change. Finally, it returns the minimum number of
 coins needed to make the given amount of change."""