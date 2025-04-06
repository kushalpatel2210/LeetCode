class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(i, j, charIndex):
            if charIndex == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[charIndex] or visited[i][j]:
                return False
            
            visited[i][j] = True

            res = False
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = res or dfs(x + i, y + j, charIndex + 1)

            visited[i][j] = False
            return res
        

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False