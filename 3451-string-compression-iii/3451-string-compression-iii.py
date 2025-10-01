class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        i = 0

        while i < len(word):
            ch = word[i]
            count = 0

            while i < len(word) and ch == word[i] and count < 9:
                i += 1
                count += 1
            
            res += str(count) + ch

        return res