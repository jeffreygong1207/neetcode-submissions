class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        #check rows
        for i in range(rows):
            total = set()
            for j in range(cols):
                cell = board[i][j]
                if cell != '.':
                    if cell in total:
                        return False
                    else:
                        total.add(cell)

        #check cols
        for i in range(cols):
            total = set()
            for j in range(rows):
                cell = board[j][i]
                if cell != '.':
                    if cell in total:
                        return False
                    else:
                        total.add(cell)

        # check 3 x 3 
        for i in range(0,9,3):
            for j in range(0,9,3):
                #i, j is starting
                total = set()
                for l in range(i, i+3):
                    for k in range(j, j +3):
                        cell = board[l][k]
                        if cell != '.':
                            if cell in total:
                                return False
                            else:
                                total.add(cell)



        return True
        