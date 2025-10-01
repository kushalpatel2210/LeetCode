class Solution:
    def isNumber(self, s):
        return s.lstrip('-').isdigit()

    def getTokens(self, expr):
        curr, tokens, bal = [], [], 0

        for c in expr:
            if c == '(':
                bal += 1
                curr.append(c)
            elif c == ')':
                bal -=1 
                curr.append(c)
            elif c == " " and bal == 0:
                if curr:
                    tokens.append("".join(curr))
                    curr = []
            else:
                curr.append(c)

        if curr:
            tokens.append("".join(curr))
        
        return tokens
    
    def helper(self, expr, env):
        if expr != '(':
            if self.isNumber(expr):
                return int(expr)
            for scope in reversed(env):
                if expr in scope:
                    return scope[expr]

        expr = expr[1:-1] # remove outer parenthasis
        tokens = self.getTokens(expr)
        op = tokens[0]

        if op == "add":
            return self.helper(tokens[1], env) + self.helper(tokens[2], env)
        elif op == "mult":
            return self.helper(tokens[1], env) * self.helper(tokens[2], env)
        elif op == "let":
            newEnv = env + [{}]
            for i in range(1, len(tokens) - 1, 2):
                var, varExpr = tokens[i], tokens[i + 1]
                val = self.helper(varExpr, newEnv)
                newEnv[-1][var] = val
            return self.helper(tokens[-1], newEnv)

    def evaluate(self, expression: str) -> int:
        return self.helper(expression, [{}])