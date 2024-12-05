class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charsMapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack and stack[-1] == charsMapping.get(char):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0