from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        maxLength = 0
        freq = Counter()
        length = 0

        for j in range(len(s)):
            currentChar = s[j]
            freq[currentChar] += 1

            while freq[currentChar] != 1:
                # shrink window
                freq[s[i]] -= 1
                i += 1
            
            if j - i + 1 > maxLength:
                maxLength = j - i + 1
                length = max(length, maxLength)
        
        return maxLength