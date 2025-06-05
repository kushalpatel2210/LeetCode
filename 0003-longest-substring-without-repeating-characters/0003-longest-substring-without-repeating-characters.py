from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        l = 0
        longest = float('-inf')

        for r in range(len(s)):
            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
                    
            longest = max(longest, r - l + 1)
        
        return 0 if longest == float('-inf') else longest