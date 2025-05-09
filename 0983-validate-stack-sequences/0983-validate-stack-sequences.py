class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []

        for n in pushed:
            stack.append(n)

            while i < len(pushed) and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return not stack