from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        i = 0
        res = float('-inf')

        for j in range(len(s)):
            counter[s[j]] += 1

            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        
        return res if res != float('-inf') else 0