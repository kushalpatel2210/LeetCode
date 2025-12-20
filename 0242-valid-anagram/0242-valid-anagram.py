from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        
        return count_s == count_t

"""
Sol 1:
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = Counter(s), Counter(t)
        return count_s == count_t
"""