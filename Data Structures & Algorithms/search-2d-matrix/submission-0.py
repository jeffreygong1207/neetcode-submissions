class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols -1
        while l <= r:
            middle = (l+r)//2
            row, col = middle// cols, middle % cols
            if target > matrix[row][col]:
                l = middle + 1
            elif target < matrix[row][col]:
                r = middle - 1
            else:
                return True
        return False



        