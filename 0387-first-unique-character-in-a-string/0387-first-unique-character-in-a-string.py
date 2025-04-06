from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        
        return -1