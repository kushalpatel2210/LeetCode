class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        i = 0
        
        while i < len(word):
            ch = word[i]
            count = 0
            
            while i < len(word) and (count < 9 and word[i] == ch):
                i += 1
                count += 1
                
            res += str(count)
            res += ch

        return res
