class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = sorted(list(s))
        listT = sorted(list(t))
        return listS == listT
        