class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force approach
        # brute force price i and price j so that index at j is great than i
        # calculate the profit it can make then compare to max profit
        # update the max profit accordingly
        
        # sliding window
        []
        min_buy = [0] * len(prices)
        max_sell = [0] * len(prices)
        min_buy[0] = prices[0]
        max_sell[-1] = prices[-1]
        for i in range(1, len(prices)):
            min_buy[i] = min(prices[i], min_buy[i - 1])
        for i in range(len(prices)-2, -1, -1):
            max_sell[i] = max(prices[i], max_sell[i + 1])
        
        profits = [0] * len(prices)
        for i in range(len(prices)):
            profits[i] = max_sell[i] - min_buy[i]
        
        return max(profits)

        

            