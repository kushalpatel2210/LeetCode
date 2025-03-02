class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s: 
            return 0

        g.sort()
        s.sort()
        ptrG = ptrS = count = 0

        while ptrG < len(g) and ptrS < len(s):
            if g[ptrG] <= s[ptrS]:
                ptrG += 1
                ptrS += 1
                count += 1
            else:
                ptrS += 1
            
        return count