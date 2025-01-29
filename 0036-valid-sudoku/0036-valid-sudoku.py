class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check Each Row
        for row in board:
            duplicate = []
            for value in row:
                if value != '.':
                    if value in duplicate:
                        return False
                    duplicate.append(value)
        
        # Check Each Column
        for i in range(len(board)):
            duplicate = []
            for j in range(len(board)):
                value = board[j][i]
                if value != '.':
                    if value in duplicate:
                        return False
                    duplicate.append(value)
        
        # Check Each Box
        for square in range(9):
            duplicate = []
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    val = board[row][col]
                    if val != '.':
                        if val in duplicate:
                            return False
                        duplicate.append(val)

        return True