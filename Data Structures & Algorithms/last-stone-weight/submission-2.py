import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = [-s for s in stones]
        heapq.heapify(rocks)


        while len(rocks) > 1:
            one = heapq.heappop(rocks)
            two = heapq.heappop(rocks)
            if one == two:
                continue
            else:
                new_stone = abs(one - two)
                heapq.heappush(rocks, -new_stone)
        
        if len(rocks) == 1:
            return -rocks[0]
        else:
            return 0
            

        