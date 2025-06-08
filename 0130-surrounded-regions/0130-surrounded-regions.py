class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return

            if board[r][c] != "O":
                return 
            
            board[r][c] = 'T'

            for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + deltaI, c + deltaJ)

        # 1. Capture not surrounded regions (O to T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in (0, ROWS - 1) or c in (0, COLS - 1)):
                    dfs(r, c)

        # 2. Make surrounded regions to (O to X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. Change not surrounded regions (T to O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'