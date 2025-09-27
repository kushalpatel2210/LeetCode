class Solution:
    def is_number(self, s):
        return s.lstrip('-').isdigit()
    
    def get_tokens(self, expr):
        curr, tokens, bal = [], [], 0

        for c in expr:
            if c == '(':
                bal += 1
                curr.append(c)
            elif c == ')':
                bal -= 1
                curr.append(c)
            elif c == ' ' and bal == 0:
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
            if self.is_number(expr):
                return int(expr)
            for scope in reversed(env):
                if expr in scope:
                    return scope[expr]

        expr = expr[1:-1]
        tokens = self.get_tokens(expr)
        op = tokens[0]

        if op == 'add':
            return self.helper(tokens[1], env) + self.helper(tokens[2], env)
        elif op == 'mult':
            return self.helper(tokens[1], env) * self.helper(tokens[2], env)
        elif op == "let":
            new_env = env + [{}]
            for i in range(1, len(tokens) - 1, 2):
                var, var_expr = tokens[i], tokens[i + 1]
                val = self.helper(var_expr, new_env)
                new_env[-1][var] = val
            return self.helper(tokens[-1], new_env)

    def evaluate(self, expression: str) -> int:
        return self.helper(expression, [{}])