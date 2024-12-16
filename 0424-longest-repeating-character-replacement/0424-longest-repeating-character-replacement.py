from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        maxLength = 0 
        freq = Counter()

        for j in range(len(s)):
            char = s[j]
            freq[char] += 1

            while j - i + 1 - max(freq.values()) > k:
                # shrink window 
                freq[s[i]] -= 1 
                # if freq[s[i]] == 0:
                #     del freq[s[i]]
                i += 1
            
            if j - i + 1 > maxLength:
                maxLength = j - i + 1

        return maxLength

