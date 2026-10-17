class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        

        def reach(r, c, seen, prev):
            if (r < 0 or c < 0 or r == rows or c == cols
                    or (r, c) in seen or heights[r][c] < prev):
                #not reachable
                return
            seen.add((r,c))
            directions = [(1,0),(-1,0),(0,1), (0,-1)]
            for dr, dc in directions:
                reach(r+dr, c+dc, seen, heights[r][c])
        
        for r in range(rows):
            #check pacific and atlantic
            reach(r, 0, pacific, heights[r][0])
            reach(r, cols-1, atlantic, heights[r][cols-1])
        for c in range(cols):
            reach(0, c, pacific, heights[0][c])
            reach(rows-1, c, atlantic, heights[rows-1][c])

        return [[r,c] for r,c in pacific & atlantic]
                

        