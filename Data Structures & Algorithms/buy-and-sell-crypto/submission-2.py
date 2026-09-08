class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        if len(prices) == 1:
            return 0
        
        max_profit = 0
        for r in range(1,len(prices)):
            if prices[r] - prices[left] > max_profit:
                max_profit = prices[r]-prices[left]
            if prices[left] > prices[r]:
                left = r
    
        return max_profit
        