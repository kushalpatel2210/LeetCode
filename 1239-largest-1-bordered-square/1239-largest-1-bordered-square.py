class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        down = [[0] * cols for _ in range(rows)]
        right = [[0] * cols for _ in range(rows)]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if grid[row][col] == 1:
                    down[row][col] = 1 + (down[row + 1][col] if row + 1 < rows else 0)
                    right[row][col] = 1 + (right[row][col + 1] if col + 1 < cols else 0)
        
        for max_side in range(min(rows, cols), 0, -1):
            for row in range(rows - max_side + 1):
                for col in range(cols - max_side + 1):
                    if (down[row][col] >= max_side and right[row][col] >= max_side and down[row][col + max_side - 1] >= max_side and right[row + max_side - 1][col] >= max_side):
                        return max_side ** 2

        return 0
