class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if not (0 <= i < m and 0 <= j < n):
                return False
            
            if visited[i][j] or board[i][j] != word[idx]:
                return False
            
            visited[i][j] = True
            for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1 , 0)]:
                if dfs(i + deltaI, j + deltaJ, idx + 1):
                    return True
            
            visited[i][j] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
