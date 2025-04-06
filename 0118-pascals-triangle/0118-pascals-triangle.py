class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            previousRow = res[i - 1]
            currRow = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    currRow.append(1)
                else:
                    currRow.append(previousRow[j - 1] + previousRow[j])
            res.append(currRow)
        
        return res