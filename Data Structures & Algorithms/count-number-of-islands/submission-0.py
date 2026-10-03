class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            stack = []
            grid[row][col] = "0"
            stack.append((row, col))
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    newr = row + dr
                    newc = col + dc
                    if 0<=newr<len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] == "1":
                        stack.append((newr, newc))
                        grid[newr][newc] = '0'
                    else:
                        continue

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
                    #weve found an island 
        
        return islands



        