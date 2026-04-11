# best_time_to_buy_sell_stock.py

"""
Problem: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a stock on day i.

You want to maximize your profit by choosing:
- one day to buy
- one later day to sell

Return the maximum profit.

Example:
Input: [7,1,5,3,6,4]
Output: 5  (Buy at 1, Sell at 6)

Approach (Greedy):
- Track minimum price so far
- Calculate profit at each step
- Keep updating max profit

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit


# -------------------------------
# Test Cases
# -------------------------------

prices1 = [7, 1, 5, 3, 6, 4]
print("Output:", max_profit(prices1))  # 5

prices2 = [7, 6, 4, 3, 1]
print("Output:", max_profit(prices2))  # 0
