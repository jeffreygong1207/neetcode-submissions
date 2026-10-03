from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #count the fresh fruit 
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        fruits = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    fruits.append((r,c))
        
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        minutes = 0
        while fruits and fresh > 0:
            minutes += 1
            n = len(fruits)
            for _ in range(n):
                r, c = fruits.popleft()
                for dr, dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc] ==1:
                        grid[newr][newc] = 2
                        fruits.append((newr, newc))
                        fresh -= 1
        
        if fresh > 0:
            print(fresh)
            return -1
        else:
            return minutes
            

            

                

        