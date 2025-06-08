class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            
            if not (0 <= i < ROWS and 0 <= j < COLS) or visited[i][j]:
                return False
            
            if board[i][j] != word[idx]:
                return False

            visited[i][j] = True

            for dI, dJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nI, nJ = i + dI, j + dJ
                if dfs(nI, nJ, idx + 1):
                    return True

            visited[i][j] = False
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
        