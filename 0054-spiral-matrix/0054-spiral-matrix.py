class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []

        while l <= r and t <= b:
            # left to right
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1

            # top to bottom
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            if not (l <= r and t <= b):
                break

            # right to left
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1

            # bottom to top
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res