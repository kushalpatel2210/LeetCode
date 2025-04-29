class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)] 
        
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            
            if not (0 <= i < m and 0 <= j < n):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[i][j]
        
        return dfs(0, 0)

