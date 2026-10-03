class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        from collections import deque
        q = deque()

        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

            
        while q:
            row, col = q.popleft()
            for dr ,dc in directions:
                newr = row +dr
                newc = col + dc
                if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc] == 2147483647:

                    q.append((newr,newc))
                    grid[newr][newc] = grid[row][col] + 1


        




       
            
        