from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        while q:
            rottenOranges = len(q)
            rottenOrange = False

            for _ in range(rottenOranges):
                i, j = q.popleft()
                
                for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newI, newJ = i + deltaI, j + deltaJ
                    if 0 <= newI < rows and 0 <= newJ < cols and grid[newI][newJ] == 1:
                        freshOranges -= 1
                        grid[newI][newJ] = 2
                        q.append((newI, newJ))
                        rottenOrange = True
                
            if rottenOrange:
                minutes += 1

        return minutes if freshOranges == 0 else -1