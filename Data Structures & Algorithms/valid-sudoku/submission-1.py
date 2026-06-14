class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRows = collections.defaultdict(set)
        seenCols = collections.defaultdict(set)
        seenSubsquare = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in seenRows[r] 
                or board[r][c] in seenCols[c] 
                or board[r][c] in seenSubsquare[(r // 3, c // 3)]):
                    return False
                
                seenRows[r].add(board[r][c])
                seenCols[c].add(board[r][c])
                seenSubsquare[(r // 3, c // 3)].add(board[r][c])

        return True

                
