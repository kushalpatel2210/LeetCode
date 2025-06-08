class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])

        if originalColor == color:
            return image

        def dfs(i, j):
            if not (0 <= i < ROWS and 0 <= j < COLS):
                return 
            
            if image[i][j] != originalColor:
                return 
            
            image[i][j] = color

            for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + deltaI, j + deltaJ)
        
        dfs(sr, sc)

        return image