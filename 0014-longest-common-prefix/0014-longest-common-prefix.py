class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        currWord = strs[0]

        for i, char in enumerate(currWord):
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return res
            res += char

        return res