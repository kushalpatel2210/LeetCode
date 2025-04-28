class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j, charIndex):
            if charIndex == len(word):
                return True
            
            if not (0 <= i < rows and 0 <= j < cols):
                return False
            
            if visited[i][j] or board[i][j] != word[charIndex]:
                return False
            
            visited[i][j] = True
            res = False

            for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = res or dfs(i + deltaI, j + deltaJ, charIndex + 1)

            visited[i][j] = False
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
            