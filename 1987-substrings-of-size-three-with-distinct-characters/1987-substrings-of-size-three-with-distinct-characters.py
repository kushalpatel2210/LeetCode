from collections import defaultdict

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        count = 0
        freq = defaultdict(int)
        k = 3

        for j in range(len(s)):
            freq[s[j]] += 1

            if j - i + 1 < k:
                continue
            
            # business logic
            if len(freq) == k:
                count += 1

            # slide window
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
            i += 1
        
        return count