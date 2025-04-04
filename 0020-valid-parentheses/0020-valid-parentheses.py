class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for c in s:
            if c in parentheses:
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

