class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return False
            
            grid[i][j] = 0

            for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newI, newJ = i + deltaI, j + deltaJ
                if 0 <= newI < n and 0 <= newJ < m and grid[newI][newJ] == "1":
                    dfs(newI, newJ)
            
            return True
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands