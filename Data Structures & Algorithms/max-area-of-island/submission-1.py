class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:



        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(row, col):
            nonlocal size
            if 0<= row<len(grid) and 0<=col<len(grid[0]) and grid[row][col] == 1:
                #valid
                size += 1
                grid[row][col] = 0
            else:
                return
            for dr, dc in directions:
                dfs(row+dr,col+dc)

        max_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    size = 0
                    dfs(r,c)
                    max_size = max(size, max_size)
        return max_size
        

        