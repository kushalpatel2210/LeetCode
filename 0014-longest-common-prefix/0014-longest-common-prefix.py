class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currWord = strs[0]
        res = ""

        for i, c in enumerate(currWord):
            for word in strs:
                if i >= len(word) or word[i] != c:
                    return res
            res += c
        
        return res
