class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        m, n = len(image), len(image[0])

        def dfs(i, j): 
            if not (0 <= i < m and 0 <= j < n) or image[i][j] == color or image[i][j] != originalColor:
                return
            
            image[i][j] = color

            for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + deltaI, j + deltaJ)

        dfs(sr, sc)

        return image