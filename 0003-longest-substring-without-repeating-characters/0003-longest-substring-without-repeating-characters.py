from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        l = 0
        maxLength = 0

        for r in range(len(s)):
            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1 
            
            maxLength = max(maxLength, r - l + 1)     
        
        return maxLength
