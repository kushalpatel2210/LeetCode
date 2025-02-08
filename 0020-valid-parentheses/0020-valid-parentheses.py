class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []

        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            elif stack and hashMap[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if len(stack) == 0 else False
