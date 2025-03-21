class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if (char.islower() and char.upper() == stack[-1]) or (char.isupper() and char.lower() == stack[-1]):
                    stack.pop()
                else: 
                    stack.append(char)
                                    
        return "".join(stack)