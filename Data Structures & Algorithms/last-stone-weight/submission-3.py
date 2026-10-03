import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = [-s for s in stones]
        heapq.heapify(rocks)
 
        while len(rocks) > 1:
            stone1 = -heapq.heappop(rocks)
            stone2 = -heapq.heappop(rocks)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(rocks, -abs(stone1-stone2))
        if rocks:
            return -rocks[0]
        return 0
        