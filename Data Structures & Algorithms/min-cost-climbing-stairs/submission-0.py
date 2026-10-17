class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0]* len(cost)
        costs[0] = cost[0]
        costs[1] = cost[1]

        for i in range(2,len(cost)):
            costs[i] = cost[i] + min(costs[i-2], costs[i-1])
        
        return min(costs[-1], costs[-2])
        