class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rowSet = set()
        # colSet = set()
        # gridSet = set()

        # for r in range(len(board)):
        #     rowSet.add(board)
        #     for c in range(len(board[r])):
        #         rowSet.add(board[r][c])
        #         colSet.add(board[r][c])
        #         gridSet.add(board[r][c])

        for r in range(len(board)):
            rowSet = set()
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet:
                    return False
                rowSet.add(board[r][c])
                
        for c in range(len(board[0])):
            colSet = set()
            for r in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colSet:
                    return False
                colSet.add(board[r][c])

        for square in range(9):
            gridSet = set()
            for row in range(3):
                for col in range(3):
                    r = (square // 3) * 3 + row
                    c = (square % 3) * 3 + col
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in gridSet:
                        return False
                    gridSet.add(board[r][c])

        return True


