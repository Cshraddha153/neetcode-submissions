class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==".":
                    continue

                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in square[(r//3, c//3)]:
                    return False
                
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[r//3, c//3].add(board[r][c])

        return True

            
        
        
                