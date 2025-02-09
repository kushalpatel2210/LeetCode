class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+' or token == '-' or token == '/' or token == '*':
                pop1 = stack.pop()
                pop2 = stack.pop()
                res = 0

                if token == '/':
                    res = int(pop2 / pop1)
                elif token == '*':
                    res = pop2 * pop1
                elif token == '-':
                    res = pop2 - pop1
                else: # '+'
                    res = pop2 + pop1

                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]