class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or image[i][j] != originalColor:
                return
            
            image[i][j] = color

            for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + deltaI, j + deltaJ)
        
        dfs(sr, sc)
        return image