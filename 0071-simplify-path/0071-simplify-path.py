class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')

        for curr in paths:
            if curr == '..' and stack:
                stack.pop()
            elif curr != '' and curr != '.' and curr != '..':
                stack.append(curr)

        return '/' + '/'.join(stack)

'''
import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        outputStack = []
        simplified = '/'
        pattern = r"[a-zA-Z._]+"

        while stack:
            curr = stack.pop()

            if curr == '' or curr == '.':
                continue
            elif curr == '..':
                count = 1
                while stack and count > 0:
                    curr_ele = stack.pop()
                    if curr_ele == '.':
                        continue
                    if curr_ele == '..':
                        count += 1
                    elif re.fullmatch(pattern, curr_ele):
                        count -= 1
            else:
                outputStack.append(curr)
                
        simplified += '/'.join(reversed(outputStack))

        return simplified
'''