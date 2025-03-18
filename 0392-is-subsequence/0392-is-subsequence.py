class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptrS, ptrT = 0, 0

        while ptrT < len(t) and ptrS < len(s):
            if s[ptrS] != t[ptrT]:
                ptrT += 1
            else:
                ptrT += 1
                ptrS += 1
        
        return ptrS == len(s)