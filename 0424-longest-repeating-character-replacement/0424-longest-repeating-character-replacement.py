class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        max_freq = 0
        max_length = 0
        left = 0

        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            max_freq = max(max_freq, charCount[s[right]])

            if (right - left + 1) - max_freq > k:
                charCount[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length