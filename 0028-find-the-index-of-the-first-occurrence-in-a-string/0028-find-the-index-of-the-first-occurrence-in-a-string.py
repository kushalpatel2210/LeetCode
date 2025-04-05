class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenh, lenn = len(haystack), len(needle)
        
        if haystack == needle:
            return 0
        
        if lenn > lenh:
            return -1
        
        for i in range(lenh - lenn + 1):
            window = i + lenn
            if haystack[i:window] == needle:
                return i
        
        return -1

        