class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystackLst = list(haystack)
        m = len(haystack)
        n = len(needle)

        if haystack == needle:
            return 0
        if n > len(haystack):
            return -1
        
        for i in range(m - n + 1):
            if "".join(haystackLst[i : i + n]) == needle:
                return i

        return - 1