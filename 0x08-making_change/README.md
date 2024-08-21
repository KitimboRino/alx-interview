**Make Change - Python Implementation**

**Overview**
The makeChange function is a Python implementation that determines the fewest number of coins needed to meet a given total using a list of coin denominations. The function is based on a dynamic programming approach to ensure optimal efficiency and correctness.

**Function Prototype**

***python***

def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total.
    
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
        
    Return:
        int: Minimum number of coins or -1 if the total cannot be met
    """
Parameters
coins: A list of integers representing the values of the coins available. The value of each coin will always be an integer greater than 0.

total: An integer representing the target total amount that needs to be achieved using the fewest number of coins.

Return Value
The function returns the minimum number of coins needed to achieve the given total.

If the total cannot be met using any combination of the given coins, the function returns -1.

If the total is 0 or less, the function returns 0 since no coins are needed.

**Example Usage**
python

coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output: 3 (11 can be made with 5 + 5 + 1)
In the example above, the total of 11 can be achieved using three coins: two 5 coins and one 1 coin.

**How It Works**

Initialization: The function initializes a dp array where each index i represents the minimum number of coins required to make the total i. The array is initialized with a large value (representing infinity) to signify that the total cannot initially be met. The base case is dp[0] = 0, since no coins are needed to achieve a total of 0.

Dynamic Programming: The function iterates over all possible totals from 1 to total. For each total, it checks each coin in the coins list. If the coin can be used to achieve the current total, the function updates the dp array with the minimum number of coins needed.

Result: After filling out the dp array, the function checks the value of dp[total]. If it is still set to infinity, it means that the total cannot be achieved with the given coins, and the function returns -1. Otherwise, it returns the value of dp[total], which is the minimum number of coins needed.

**Edge Cases**
Total is 0 or Less: The function returns 0 since no coins are needed.

Total Cannot Be Met: If no combination of coins can achieve the total, the function returns -1.

Empty Coin List: If the coin list is empty or contains no useful denominations, the function will return -1 if the total is greater than 0.

**Performance**
Time Complexity: O(n * m), where n is the total and m is the number of coin denominations. This is because for each total, the function iterates over each coin to find the minimum number of coins needed.

Space Complexity: O(n), since the space used by the dp array is proportional to the total.