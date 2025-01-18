from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countOfs, countOft = Counter(s), Counter(t)
        
        return countOfs == countOft