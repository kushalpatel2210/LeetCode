from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        l = 0
        ans = ""
        len_ans = len(s)
        counter_t = Counter(t)
        counter = Counter()

        for r in range(len(s)):
            if s[r] in t:
                counter[s[r]] += 1

            while l <= r and all(counter[ch] >= counter_t[ch] for ch in counter_t):
                if r - l + 1 <= len_ans:
                    len_ans = r - l + 1
                    ans = s[l : r + 1]
                
                if s[l] in counter:
                    counter[s[l]] -= 1

                l += 1
        
        return ans