class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')': '(', '}':'{', ']': '['}

        for c in s:
            if c in '{([':
                stack.append(c)
            else:
                if not stack or stack[-1] != hashMap[c]:
                    return False
                stack.pop()
        
        return True if not stack else False