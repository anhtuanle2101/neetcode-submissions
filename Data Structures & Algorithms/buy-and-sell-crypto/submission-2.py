'''
    choose a day to buy and a day to sell
    
    return maximum profit -> buy as low and sell as high -> if we have 2 pointers one point at a buy day and
    one for the sell day, 
    if the buy pointer is larger or equal than the sell pointer which means we make no profits
    -> buy pointer -> sell pointer and move the sell pointer to the next day
    else the buy pointer is less than the sell pointer -> we are making a profit
    - calculate profit and update max profit and move the sell pointer by one

    [10, 1, 5, 6, 7, 1]
                     *  *
    max = 6
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] >= prices[sell]:
                buy = sell
                sell += 1
                continue
            
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            sell += 1

        return max_profit