class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxProfit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)
            sell += 1
        

        return maxProfit


        

        