class Node:
    def __init__(self, type_, value=None, children=None):
        self.type = type_ # "const", "var" or "op"
        self.value = value
        self.children = children or []

class Solution:
    def is_number(self, s):
        return s.lstrip('-').isdigit()

    def get_tokens(self, expr):
        tokens, curr, bal = [], [], 0

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

    def build_tree(self, expr):
        if expr[0] != "(":
            if self.is_number(expr):
                return Node("const", int(expr))
            else:
                return Node("var", expr)
        
        expr = expr[1:-1]
        tokens = self.get_tokens(expr)
        op = tokens[0]
        children = [self.build_tree(tok) for tok in tokens[1:]]
        return Node("op", op, children)
    
    def eval_tree(self, node, env):
        if node.type == "const":
            return node.value
        
        if node.type == "var":
            for scope in reversed(env):
                if node.value in scope:
                    return scope[node.value]
        
        if node.type == "op":
            if node.value == "add":
                return self.eval_tree(node.children[0], env) + self.eval_tree(node.children[1], env)
            elif node.value == "mult":
                return self.eval_tree(node.children[0], env) * self.eval_tree(node.children[1], env)
            elif node.value == "let":
                new_env = env + [{}]

                for i in range(0, len(node.children) -1, 2):
                    var = node.children[i].value
                    val = self.eval_tree(node.children[i + 1], new_env)
                    new_env[-1][var] = val
                
                return self.eval_tree(node.children[-1], new_env)

    def evaluate(self, expression: str) -> int:
        root = self.build_tree(expression)
        return self.eval_tree(root, [{}])