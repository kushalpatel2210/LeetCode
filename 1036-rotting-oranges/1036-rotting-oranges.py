from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        minutes = 0

        for i in range(m):
            for j in range(n):
                orange = grid[i][j]
                if orange == 1:
                    freshOranges += 1
                elif orange == 2:
                    q.append((i, j))
        
        if freshOranges == 0:
            return 0

        while q:
            newRotten = False

            for _ in range(len(q)):
                i, j = q.popleft()

                for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + deltaI, j + deltaJ
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        q.append((ni, nj))
                        grid[ni][nj] = 2
                        freshOranges -= 1
                        newRotten = True
            
            if newRotten:
                minutes += 1
                        
        return minutes if freshOranges == 0 else -1