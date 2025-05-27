class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # Monolithic increasing 
        
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            
            stack.append(n)

        while stack and k:
            stack.pop()
            k -= 1
        
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1

        res = stack[i:]
        return "".join(res) if res else "0"