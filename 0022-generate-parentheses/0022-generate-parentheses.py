class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return 
            
            if open < n:
                stack.append('(')
                backtrack(open + 1, closed)
                stack.pop()
            
            if closed < open:
                stack.append(')')
                backtrack(open, closed + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
        