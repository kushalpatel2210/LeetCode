from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshOranges = 0
        q = deque()
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        if freshOranges == 0:
            return 0

        while q:
            i, j = q.popleft()
            rottenOrange = False

            for deltaI, deltaJ in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= i + deltaI < m and 0 <= j + deltaJ < n and grid[i + deltaI][j + deltaJ] == 1:
                    q.append((i + deltaI, j + deltaJ))
                    freshOranges -= 1
                    grid[i + deltaI][j + deltaJ] = 2
                    rottenOrange = True
            
            if rottenOrange:
                minutes += 1

        return minutes if freshOranges == 0 else -1
