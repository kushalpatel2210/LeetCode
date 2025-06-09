class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        r = 0
        going_down = False
        res = [''] * numRows

        for c in s:
            res[r] += c

            if r == 0 or r == numRows - 1:
                going_down = not going_down
            
            r = r + 1 if going_down else r - 1
        
        return "".join(res)