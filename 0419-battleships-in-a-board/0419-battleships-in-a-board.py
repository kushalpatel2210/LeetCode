class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(i, j):
            if not (0 <= i < ROWS and 0 <= j < COLS):
                return 
            
            if visited[i][j] or board[i][j] == '.':
                return
            
            visited[i][j] = True
            board[i][j] = '.'

            for dI, dJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + dI, j + dJ)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X':
                    dfs(r, c)
                    count += 1
        
        return count

