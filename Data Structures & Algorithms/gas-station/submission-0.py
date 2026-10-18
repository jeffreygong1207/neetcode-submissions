class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #if one solution if we go there must be a place where we are negative
        #then we take the next solution

        if sum(gas) < sum(cost):
            return -1
        current = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                current = i + 1
                tank = 0

        
        return current
        