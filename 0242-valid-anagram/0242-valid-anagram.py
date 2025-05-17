from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = defaultdict(int), defaultdict(int)

        for c in s:
            sCount[c] += 1
        
        for c in t:
            tCount[c] += 1
        
        return sCount == tCount