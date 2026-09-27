class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                best = max(profit, best)
            else:
                l = r
            r += 1
        
        
        return best

        