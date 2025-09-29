class Node:
    def __init__(self, type_, value=None, children=None):
        self.type = type_       # "Const", "Var", "Op"
        self.value = value      # integer, variable name, or operator
        self.children = children or []


class Solution:
    def is_number(self, s: str) -> bool:
        return s.lstrip('-').isdigit()

    def get_tokens(self, expr: str):
        """Tokenize keeping balanced parentheses intact."""
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

    def buildTree(self, expr: str) -> Node:
        """Parse Lisp-like string into a Node tree."""
        expr = expr.strip()
        if expr[0] != '(':
            # Base case: number or variable
            if self.is_number(expr):
                return Node("Const", int(expr))
            else:
                return Node("Var", expr)

        # Remove outer parentheses
        expr = expr[1:-1]
        tokens = self.get_tokens(expr)
        op = tokens[0]
        children = [self.buildTree(tok) for tok in tokens[1:]]
        return Node("Op", value=op, children=children)

    def evalTree(self, node: Node, env: list[dict]) -> int:
        """Evaluate AST recursively with environment (scope)."""
        if node.type == "Const":
            return node.value

        if node.type == "Var":
            for scope in reversed(env):
                if node.value in scope:
                    return scope[node.value]
            raise NameError(f"Unbound variable {node.value}")

        if node.type == "Op":
            if node.value == "add":
                return self.evalTree(node.children[0], env) + self.evalTree(node.children[1], env)

            elif node.value == "mult":
                return self.evalTree(node.children[0], env) * self.evalTree(node.children[1], env)

            elif node.value == "let":
                new_env = env + [{}]
                # assign variables in pairs, last child is final expression
                for i in range(0, len(node.children) - 1, 2):
                    var = node.children[i].value   # must be Var
                    val = self.evalTree(node.children[i+1], new_env)
                    new_env[-1][var] = val
                return self.evalTree(node.children[-1], new_env)

    def evaluate(self, expression: str) -> int:
        """Main entry (like in LeetCode)."""
        root = self.buildTree(expression)
        return self.evalTree(root, [{}])
