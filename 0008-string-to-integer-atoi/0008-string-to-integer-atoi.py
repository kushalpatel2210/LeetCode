class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        sign = None
        signCount = 0
        newS = s.lstrip()
        for i, c in enumerate(newS):
            if c == ' ':
                break

            if signCount > 1:
                break

            if len(res) == 0 and c in '+-':
                signCount += 1
                sign = c
                continue

            if c.isalpha() or c in '+-.':
                break
            
            if c.isdigit():
                res.append(c)

        if not res:
            return 0
        else:
            num = int(''.join(res))
            if sign and sign == '-':
                if -num < -(2**31):
                    return -(2**31)
                return -num
            else:
                if num > (2**31) - 1:
                    return (2**31) - 1
                return num
