class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #idea iterate through each cell
        #if we see a O we run dfs until we reach a border, if we do we cant surround
        protect = set()
        def dfs(r,c):
            nonlocal protect
            if (r,c) in protect or r < 0 or c < 0 or r == rows or c == cols or board[r][c] == "X":
                return
            protect.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r+dr,c+dc)
            
        
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            #check left and right boarders
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            #check top and bottom borders
            dfs(0,c)
            dfs(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in protect:
                    board[r][c] = "X"
        