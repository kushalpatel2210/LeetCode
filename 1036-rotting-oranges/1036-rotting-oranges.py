from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshOranges = 0
        q = deque()
        minutes = 0

        for i in range(m):
            for j in range(n):
                orange = grid[i][j]

                if orange == 2:
                    q.append((i, j))
                elif orange == 1:
                    freshOranges += 1
        
        if freshOranges == 0:
            return 0
        
        while q:
            totalOranges = len(q)
            rottenOrange = False

            for _ in range(totalOranges):
                i, j = q.popleft()

                for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newI, newJ = i + deltaI, j + deltaJ
                    if 0 <= newI < m and 0 <= newJ < n and grid[newI][newJ] == 1:
                        freshOranges -= 1
                        q.append((newI, newJ))
                        grid[newI][newJ] = 2
                        rottenOrange = True
                
            if rottenOrange:
                minutes += 1
        
        return -1 if freshOranges else minutes


