class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num1, num2 = stack.pop(), stack.pop()
                ans = None
                if token == '*':
                    ans = num2 * num1
                elif token == '/':
                    ans = int(num2 / num1)
                elif token == '-':
                    ans = num2 - num1
                else:
                    ans = num2 + num1
                stack.append(ans)
        
        return stack.pop()