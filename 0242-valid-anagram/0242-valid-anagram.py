from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = Counter(s), Counter(t)
        return s_counter == t_counter