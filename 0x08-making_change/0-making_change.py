#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total.

    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met

    Return:
        int: Minimum number of coins or -1 if the total cannot be met
    """
    if total <= 0:
        return 0

    # Initialize dp array with a large value representing "infinity"
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for a total of 0

    # Iterate over all totals from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
