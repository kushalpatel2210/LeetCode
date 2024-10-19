class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenOfS, lenOfT = len(s), len(t)
        pointerS, pointerT = 0, 0

        if lenOfS > lenOfT:
            return False
        
        if s == "":
            return True

        while pointerT < lenOfT:
            if pointerS < lenOfS and t[pointerT] == s[pointerS]:
                if pointerS == lenOfS - 1:
                    return True
                pointerS += 1
            pointerT += 1
        
        return False

