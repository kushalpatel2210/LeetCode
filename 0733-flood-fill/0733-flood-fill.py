class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        originalColor = image[sr][sc]

        def dfs(i, j):
            print(i, j)
            if i < 0 or j < 0 or i >= rows or j >= cols or image[i][j] != originalColor or image[i][j] == color:
                return

            image[i][j] = color
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + x, j + y)
        
        dfs(sr, sc)

        return image