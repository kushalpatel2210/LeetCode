class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for char in s:
            if char in hashMap:
                if not stack or stack[-1] != hashMap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return True if not stack else False
