class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force approach
        # brute force price i and price j so that index at j is great than i
        # calculate the profit it can make then compare to max profit
        # update the max profit accordingly
        
        # sliding window
        # keep two pointers l and r with l being the buy day and r being the sell day
        # starting off l = 0 and r = 1
        # check if prices[r] > prices[l], to have a positive profit
        # if assign l = r, and r = r + 1
        # otherwise, calculate the profit and update max_profit
        # until the r < len(prices)

        if len(prices) < 2:
            return 0
        max_profit = 0
        l, r =0, 1
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r = r + 1
                continue
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            r += 1

        return max_profit

        

            