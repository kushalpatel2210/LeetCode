from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        freq = Counter()

        for r in range(len(s)):
            currChar = s[r]
            freq[currChar] += 1

            while freq[currChar] > 1:
                freq[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength