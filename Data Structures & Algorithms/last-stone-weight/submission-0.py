class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-s for s in stones]
        heapq.heapify(new_stones)
        while len(new_stones) > 1:
            stone_x = -1 * heapq.heappop(new_stones)
            stone_y = -1 * heapq.heappop(new_stones)
            if stone_y < stone_x:
                new_stone = stone_x -  stone_y
                heapq.heappush(new_stones, -new_stone)
        
        if len(new_stones) == 0:
            return 0
        else:
            return -heapq.heappop(new_stones)
            
        