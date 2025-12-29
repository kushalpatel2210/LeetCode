from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        min_window = float('inf')
        count_t, count_s = Counter(t), Counter() # empty
        have, need = 0, len(count_t)
        res = [-1, -1] # pointers

        for r in range(len(s)):
            curr = s[r]
            count_s[curr] += 1

            if curr in count_t and count_s[curr] == count_t[curr]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_window:
                    res = [l, r]
                    min_window = r - l + 1
                
                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l: r + 1] if min_window != float('inf') else ""
