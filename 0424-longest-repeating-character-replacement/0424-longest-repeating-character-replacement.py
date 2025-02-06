from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxLength = 0
        freq = Counter()

        for r in range(len(s)):
            currChar = s[r]
            freq[currChar] += 1

            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength