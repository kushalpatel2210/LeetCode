from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = Counter(s), Counter(t)

        return countS == countT