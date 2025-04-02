from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val != '.':
                    if val in rows[i] or val in cols[j] or val in squares[(i // 3, j // 3)]:
                        return False
                    
                    rows[i].add(val)
                    cols[j].add(val)
                    squares[(i // 3, j // 3)].add(val)
            
        return True