from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLength = 0
        frq = Counter()

        for r in range(len(s)):
            frq[s[r]] += 1

            while (r - l + 1 - max(frq.values())) > k:
                frq[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength