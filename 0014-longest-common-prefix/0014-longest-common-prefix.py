class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        currentWord = strs[0]

        for i, char in enumerate(currentWord):
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return res
            res += char

        return res