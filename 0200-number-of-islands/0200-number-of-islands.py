class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return
            
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + deltaI, j + deltaJ)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count