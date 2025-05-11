from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        i = 0 
        maxLength = 0

        for j in range(len(s)):
            char = s[j]
            hashMap[char] += 1

            while hashMap[char] > 1:
                hashMap[s[i]] -= 1
                i += 1
            
            maxLength = max(maxLength, j - i + 1)
        
        return maxLength
        