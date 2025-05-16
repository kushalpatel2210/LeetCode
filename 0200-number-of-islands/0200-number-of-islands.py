class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            for deltaI, deltaJ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newI, newJ = i + deltaI, j + deltaJ
                dfs(newI, newJ)
        
        noOfIslands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    noOfIslands += 1
        
        return noOfIslands
