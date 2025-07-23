class Solution: 
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        gain = 0

        if x > y: # ab
            for c in s:
                if stack and stack[-1] == 'a' and c == 'b':
                    gain += x
                    stack.pop()
                else:
                    stack.append(c)
            
            new_s = ''.join(stack)
            stack.clear()

            for c in new_s:
                if stack and stack[-1] == 'b' and c == 'a':
                    gain += y
                    stack.pop()
                else:
                    stack.append(c)

        else: # ba
            for c in s:
                if stack and stack[-1] == 'b' and c == 'a':
                    gain += y
                    stack.pop()
                else:
                    stack.append(c)
            
            new_s = ''.join(stack)
            stack.clear()

            for c in new_s:
                if stack and stack[-1] == 'a' and c == 'b':
                    gain += x
                    stack.pop()
                else:
                    stack.append(c)
        
        return gain