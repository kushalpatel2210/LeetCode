class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        i = 0

        while i < len(chars):
            currChar = chars[i]
            count = 0

            while i < len(chars) and chars[i] == currChar:
                count += 1
                i += 1
            
            chars[res] = currChar
            res += 1
            if count > 1:
                for s in str(count):
                        chars[res] = s
                        res += 1
        
        return res
            
