class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        islands = 0

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 
            if visited[i][j] or grid[i][j] == '0':
                return
            
            visited[i][j] = True

            for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + deltaI, j + deltaJ)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and visited[r][c] == False:
                    islands += 1
                    dfs(r, c)

        return islands
