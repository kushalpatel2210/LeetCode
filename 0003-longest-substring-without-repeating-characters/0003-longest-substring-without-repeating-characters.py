from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        hashMap = defaultdict(int)
        start = 0

        for i in range(len(s)):
            hashMap[s[i]] += 1

            while hashMap[s[i]] > 1:
                hashMap[s[start]] -= 1
                start += 1

            maxLength = max(maxLength, i - start + 1)

        return maxLength



