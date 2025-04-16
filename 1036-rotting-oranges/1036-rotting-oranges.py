from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        minutes = 0
        fresh_oranges = 0 

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                positions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

                for direct_row, direct_col in positions:
                    new_row, new_col = row + direct_row, col + direct_col
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh_oranges -= 1

        return minutes - 1 if fresh_oranges == 0 else -1